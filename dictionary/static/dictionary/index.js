window.onload = () => {
	// document.querySelector ('#prefix').addEventListener ('change', onChangeHandler)
	document.querySelector ('#prefix').addEventListener ('keyup',  onKeyupHandler)
}

function onKeyupHandler(argument) {

	prefixElement = document.querySelector ('#prefix')
	prefix = prefixElement.value

	if (prefix.length >= 3) {
		fetch ("entries/complete.json?prefix=" + prefix)
			.then (response => response.json ())
			.then (data => {
				// console.log (data);
				completions = data ['results'].map (result => result['text'])

				text = completions.join (' ')
				HtmlElement
				var completionElement = document.getElementById ('completions')
				completionElement.innerHTML = text
		
			})
			.catch (errors => {
				console.log (errors)
			})
	}
}

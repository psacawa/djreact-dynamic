function onChangeHandler(argument) {
	// console.log ("in onChangeHandler")

	prefixTag = document.getElementById ('prefix')
	prefix = prefixTag.value
	console.log (prefix)

	fetch ("entries/complete.json?prefix=" + prefix)
		.then (response => response.json ())
		.then (data => {
			console.log (data);
			completions = data ['results'].map (result => result['text'])
			text = completions.join ()
			var completionTag = document.getElementById ('completions')
			completionTag.innerHTML = text
		})
		.catch (errors => {
			console.log (errors)
		})
}

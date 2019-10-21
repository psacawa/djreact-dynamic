window.onload = () => {
	// document.querySelector ('#prefix').addEventListener ('change', onChangeHandler)
	document.querySelector ('#prefix').addEventListener ('keyup',  onKeyupHandler)
}

function onKeyupHandler(argument) {

	prefixElement = document.querySelector ('#prefix')
	currentPrefix= prefixElement.value

	if (currentPrefix.length >= 3) {
		if (typeof (this.timeoutID) === 'number' ) {
			// console.log (`timer already set ${this.timeoutID}`)
			window.clearTimeout (this.timeoutID)
		}
		this.timeoutID = window.setTimeout (function (prefix) {
			fetch ("entries/complete.json?prefix=" + prefix)
				.then (response => response.json ())
				.then (data => {
					completions = data ['results'].map (result => result['text'])
					text = completions.join (' ')
					// console.log (text)

					var completionElement = document.getElementById ('completions')
					while (completionElement.firstChild)
						completionElement.removeChild (completionElement.firstChild)
					for (const comp of completions) {
						childNode = document.createElement ('li')	
						childNode.innerHTML = comp
						completionElement.appendChild (childNode)
					}
					this.timeoutID = undefined
				})
				.catch (errors => {
					console.log ('in the error code')
					console.error (errors)
				})
		}.bind (this), 200, currentPrefix)
		// console.log (`set timer: ${this.timeoutID}`)
	} else {
		var completionElement = document.getElementById ('completions')
		while (completionElement.firstChild)
			completionElement.removeChild (completionElement.firstChild)
	}
}

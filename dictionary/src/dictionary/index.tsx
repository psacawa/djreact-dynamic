window.onload = () => {
  // document.querySelector ('#prefix').addEventListener ('change', onChangeHandler)
  document.querySelector ('#prefix').addEventListener ('keyup',  onKeyupHandler)
}

function onKeyupHandler(event:any) {

  const prefixElement : Element = document.querySelector ('#prefix')
  const currentPrefix = prefixElement.getAttribute('value')
  console.log (currentPrefix)

  if (currentPrefix.length >= 3) {
    if (typeof (this.timeoutID) === 'number' ) {
      // console.log (`timer already set ${this.timeoutID}`)
      window.clearTimeout (this.timeoutID)
    }
    this.timeoutID = window.setTimeout (function (prefix:string) {
      fetch ("entries/complete.json?prefix=" + prefix)
        .then (response => response.json ())
        .then (data => {
          // console.log ('fetch succeeded');
          let completions = data ['results'].map ((result:any) => Object ({
            text : result['text'],
            score : result['score']
          }));
          // console.log (completions)
          var completionElement = document.getElementById ('completions')
          while (completionElement.firstChild)
            completionElement.removeChild (completionElement.firstChild)
          for (const comp of completions) {
            let childNode = document.createElement ('li') 
            // childNode.innerHTML = comp['text'] + ' ' + comp['score']
            childNode.innerHTML = comp['text'] 
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

updateVisitCount();
function updateVisitCount() {
    fetch('https://jhln209u2i.execute-api.us-east-1.amazonaws.com/default/visitors')
        .then(response => {
        return response.json()
      })
        .then(data => {
            console.log(data)
            document.getElementById('count').innerHTML = data.visits;
        })
    }
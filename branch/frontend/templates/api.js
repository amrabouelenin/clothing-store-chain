listProudcts()
    
function listProudcts(){

    // the element the will be filled by ajax
    var wrapper = document.getElementById('list-wrapper')

    // create api call to server endpoint
    
    var API_ENDPOINT = 'http://127.0.0.1:8000/api/list/products/'


    // make the call
    fetch(API_ENDPOINT).then((resp)=>resp.json()).then(function(data){
        // console.log('Data:', data)
        // now iterate through the data and put it in table
        for (var i in data){

            try {
                document.getElementById(`data-row-${i}`).remove()
            } catch (error) {
                
            }

            var id = `<span class="title">${data[i].id}</span>`
            var name = `<span class="title">${data[i].name}</span>`
            var price = `<span class="title">${data[i].price}</span>`
            var serial =  parseInt(i)
            //console.log(serial)
            // generate html row from above data
            var row = `
                    <tr id="data-row-${serial}" class="task-wrapper flex-wrapper">
                        <th scope="row">${serial}</th>
                        <td>${id}</td>
                        <td>${name}</td>
                        <td>${price}</td>
                    </tr>
                `
            //console.log(row)
            wrapper.innerHTML += row
        }
    })
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken')
// handle submit button
var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function(e){
    
    // prevent submittion to handle it through ajax
    e.preventDefault()

    var API_ENDPOINT = 'http://127.0.0.1:8000/api/add/product/'

    // check values 
    var name = document.getElementById('name').value
    var price = document.getElementById('price').value

    // make the call
    fetch(API_ENDPOINT, { 
        
        // put the credential here
        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'name':name, 'price':price})


    }).then(function(response){
            console.log(response)
            // update the list after adition
            listProudcts()
            // reset the form elements
            document.getElementById('form').reset()

    })
    
})

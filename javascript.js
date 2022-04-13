var url = "http://127.0.0.1:5000/view";
var id = "view";

async function generator(url, id) {
    var request = await new XMLHttpRequest()

request.open('GET', url, true)
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
view(data, request, id);

}

request.send()
  }

  function view(data, request, id){
      if(id == "view"){
    if (request.status >= 200 && request.status < 400) {
         data.forEach((query) => {
          console.log(request.status);
          var div = document.createElement("tr");
            var mainContainer = document.getElementById(id);
          div.innerHTML = "<td>"+query.id+"</td><td><input id='keresztnev"+query.id+
          "' placeholder='"+query.keresztnev+"' value='"+query.keresztnev+"'/></td><td><input id='vezeteknev"+query.id+"' placeholder='"+query.vezeteknev+"' value='"+query.vezeteknev+
          "'/></td><td><input id='lakcim"+query.id+"' placeholder='"+query.lakcim+"' value='"+query.lakcim+
          "'/></td>"+"<td><input id='Osztaly"+query.id+"' placeholder='"+query.Osztaly+"' value='"+query.Osztaly+
          "'/></td><td><input id='Igazolvanyszam"+query.id+"' placeholder='"+query.Igazolvanyszam+"' value='"+query.Igazolvanyszam+
          "'/></td>"+"<button onclick = 'deleterecord("+query.id+")' type = 'submit' value='Submit'>Delete</button>"+"<button onclick = 'update("+query.id+
          ")' type = 'submit' value='Submit'>Update</button>" ;
          mainContainer.appendChild(div)
        })
      } else {
        console.log('error')
      }}
  }

async function generate_html(){
await generator(url, id);
}

function deleterecord(id){
  const data = JSON.stringify({
    id: parseInt(id)
  });
  
  navigator.sendBeacon('http://127.0.0.1:5000/deleterecord/', data);
  console.log(data);
}
function update(id){
  const data = JSON.stringify({
    id: id,
    keresztnev: document.getElementById("keresztnev"+id).value,
    vezeteknev: document.getElementById("vezeteknev"+id).value,
    lakcim: document.getElementById("lakcim"+id).value,
    Osztaly: document.getElementById("Osztaly"+id).value,
    Igazolvanyszam: document.getElementById("Igazolvanyszam"+id).value
  });

  navigator.sendBeacon('http://127.0.0.1:5000/updatedetails/', data);
  console.log(data);
}

generate_html();


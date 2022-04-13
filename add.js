function sendPost(){
    const data = JSON.stringify({
        keresztnev: document.getElementById("keresztnev").value,
        vezeteknev: document.getElementById("vezeteknev").value,
        lakcim:document.getElementById("lakcim").value,
        Osztaly: document.getElementById("Osztaly").value,
        Igazolvanyszam: document.getElementById("Igazolvanyszam").value
      });
      
      navigator.sendBeacon('http://127.0.0.1:5000/savedetails/', data);
      console.log(data);
    }
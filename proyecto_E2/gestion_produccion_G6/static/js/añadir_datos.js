let botones_ver = document.querySelectorAll(".boton_ver");
let lista_general = document.getElementById("lista");
// console.log(lista_general);

for (let boton of botones_ver) {
    boton.addEventListener('click', añadir_objetos);
}

function añadir_objetos(event) {
    event.preventDefault();
    let boton = event.currentTarget;
    let pk = boton.dataset.pk;
    let listilla = document.getElementById(pk);
    listilla.innerHTML= "";
    let botones = document.getElementById("botones"+pk);
    // console.log(listilla)
    // console.log("pk =", pk);
    let url = "/api/clientes/" + pk;
    // console.log(url);
    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (let clave in data)
            {
                if (clave == "Nombre")
                {

                }
                else if (Array.isArray(data[clave]))
                {
                    let lista_array = document.createElement("ul");
                    for (let dato of data[clave])
                    {
                        let fila_array = createElement("li")
                        fila_array.textContent = dato;
                        lista_array.append(fila_array);
                    }
                    listilla.append(lista_array);
                }
                else
                {
                    let fila_listilla = document.createElement("li");
                    fila_listilla.textContent = clave + ": " + data[clave];
                    listilla.append(fila_listilla);
                }
                let botones_editar = document.querySelectorAll(".boton_editar");
                let boto_eliminar = document.querySelectorAll(".boton_eliminar");
                listilla.append(botones_ver[0], botones_editar[0], boto_eliminar[0]);

            }
            

        })
        .catch(error => console.error('Error fetching clientes:', error));
}




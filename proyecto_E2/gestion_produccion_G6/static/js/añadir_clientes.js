let botones_ver = document.querySelectorAll(".boton_ver");

for (let boton of botones_ver) {
    boton.addEventListener('click', evento);
}


function evento(event)
{
    let boton_ver = event.currentTarget;
    let pk = boton_ver.dataset.pk;
    let final = document.getElementById("final" + pk);
    if (boton_ver.textContent == "Dejar de ver")
    {
        borrar_objetos(event,boton_ver,pk)
    } 
    else añadir_objetos(event,boton_ver,pk,final);
}
function añadir_objetos(event,boton_ver,pk,final) {
    event.preventDefault();
    let url = "/api/clientes/" + pk;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (let clave in data) {
                if (Array.isArray(data[clave])) {
                    let titulo_array = document.createElement("li");
                    titulo_array.textContent = "Proyectos:";
                    titulo_array.classList = "añadido" + pk;
                    final.appendChild(titulo_array);

                    let lista_array = document.createElement("ul");
                    lista_array.className = "añadido" + pk;

                    if (data[clave].length === 0) {
                        let no_datos = document.createElement("li");
                        no_datos.textContent = "No existen proyectos asociados";
                        lista_array.append(no_datos);
                    } else {
                        for (let dato of data[clave]) {
                            let fila_array = document.createElement("li");
                            fila_array.textContent = dato.nombre;
                            lista_array.append(fila_array);
                        }
                    }

                    final.appendChild(lista_array);
                } else {
                    let nueva_fila = document.createElement("li");
                    nueva_fila.className= "añadido" + pk;
                    nueva_fila.textContent = clave + ": " + data[clave];
                    final.appendChild(nueva_fila);
                    boton_ver.textContent = "Dejar de ver"
                }
            }
        })
        .catch(error => console.error('Error fetching clientes:', error));
}

function borrar_objetos(event,boton_ver,pk)
{
    event.preventDefault();
    let nuevos = document.getElementsByClassName("añadido" + pk)

    for (let nuevo of nuevos)
    {
        nuevo.innerHTML = "";
    }

    boton_ver.textContent = "Ver";
}



let botones_ver = document.querySelectorAll(".boton_ver");

for (let boton of botones_ver) {
    boton.addEventListener('click', añadir_objetos);
}

function añadir_objetos(event) {
    event.preventDefault();

    let boton_ver = event.currentTarget;
    let pk = boton_ver.dataset.pk;
    let final = document.getElementById("final" + pk);
    let url = "/api/clientes/" + pk;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (let clave in data) {
                if (Array.isArray(data[clave])) {
                    let fila_listilla = document.createElement("li");
                    fila_listilla.textContent = "Proyectos:";
                    final.appendChild(fila_listilla);

                    let lista_array = document.createElement("ul");

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
                    let fila_listilla = document.createElement("li");
                    fila_listilla.textContent = clave + ": " + data[clave];
                    final.appendChild(fila_listilla);
                }
            }
        })
        .catch(error => console.error('Error fetching clientes:', error));
}



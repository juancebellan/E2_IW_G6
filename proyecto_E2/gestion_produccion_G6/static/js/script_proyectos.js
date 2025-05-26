let botones_ver = document.querySelectorAll(".boton_ver");
let fotos = document.getElementsByClassName("corazon");
let favoritos = [];
let boton_favorito = document.getElementById("favoritos");
boton_favorito.addEventListener('click', evento_favoritos);

for (let boton of botones_ver) {
    boton.addEventListener('click', evento_ver);
}

for (let foto of fotos) {
    foto.addEventListener('click', eventofoto);
}


function evento_ver(event) {
    let boton_ver = event.currentTarget;
    let pk = boton_ver.dataset.pk;
    let final = document.getElementById("final" + pk);
    console.log(pk);
    if (boton_ver.textContent == "Dejar de ver") {
        borrar_objetos(event, boton_ver, pk)
    }
    else añadir_objetos(event, boton_ver, pk, final);
}
function añadir_objetos(event, boton_ver, pk, final) {
    event.preventDefault();
    console.log(pk)
    let url = "/api/proyectos/" + pk;
    console.log(final.textContent)

    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (let clave in data) {
                if (Array.isArray(data[clave])) {
                    let titulo_array = document.createElement("li");
                    titulo_array.textContent = clave + ": ";
                    titulo_array.classList = "añadido" + pk;
                    final.appendChild(titulo_array);

                    let lista_array = document.createElement("ul");
                    lista_array.className = "añadido" + pk;

                    if (data[clave].length === 0) {
                        let no_datos = document.createElement("li");
                        if (clave == "Tareas") {
                            no_datos.textContent = "No existen tareas asociadas";
                        }
                        else
                            no_datos.textContent = "No existen proyectos asociados";
                        lista_array.append(no_datos);
                    } else {
                        for (let dato of data[clave]) {
                            let fila_array = document.createElement("li");
                            fila_array.textContent = dato;
                            lista_array.append(fila_array);
                        }
                    }

                    final.appendChild(lista_array);
                } else {
                    let nueva_fila = document.createElement("li");
                    nueva_fila.className = "añadido" + pk;
                    nueva_fila.textContent = clave + ": " + data[clave];
                    final.appendChild(nueva_fila);
                    boton_ver.textContent = "Dejar de ver"
                }
            }
        })
        .catch(error => console.error('Error fetching clientes:', error));
}

function borrar_objetos(event, boton_ver, pk) {
    event.preventDefault();
    let nuevos = document.getElementsByClassName("añadido" + pk)

    for (let nuevo of nuevos) {
        nuevo.innerHTML = "";
    }

    boton_ver.textContent = "Ver";


}



function eventofoto(event) {

    let foto = event.currentTarget;
    let pk = foto.dataset.pk;
    console.log(pk)
    let lista = document.getElementById(pk);
    console.log(lista.id);
    if (foto.src == "http://127.0.0.1:8000/static/images/nolike.png") {
        foto.src = "/static/images/like.png";
        favoritos.push(lista);
    }
    else {
        foto.src = "/static/images/nolike.png";
        let index = favoritos.findIndex(favorito => favorito.id === lista.id);
        if (index !== -1) {
            favoritos.splice(index, 1);
        }

    }
    console.log(favoritos)

}
function evento_favoritos(event)
{
    event.preventDefault();
   let boton = event.currentTarget
   let listas = document.getElementsByClassName("lista");
   if (boton.textContent == "Ver solo favoritos")
   {
    mostrarFavoritos(event,listas,boton);
   }
   else mostrarTodos(event,listas,boton)
}

function mostrarFavoritos(event,listas,boton)
{
    let salvar;

    for (let lista of listas)
    {
        
        for (let favorito of favoritos)
        {
            if (lista.id == favorito.id)
            {
                salvar = true;
            }
        }
        if (!salvar)
        {
            lista.style.display = "none";
        }
        salvar = false;
    }
    boton.textContent= "Mostrar todo";
}

function mostrarTodos(event,listas,boton)
{
    for (let lista of listas)
    {
        lista.style.display = "block";
    }
    boton.textContent= "Ver solo favoritos";
}
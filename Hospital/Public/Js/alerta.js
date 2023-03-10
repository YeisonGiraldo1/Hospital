function borrar(id){
    swal({
  title: "Estas seguro que quieres borrar?",
  text: "La informacion que borres no la puedes recuperar!",
  icon: "warning",
  buttons: ["Cancelar", true],
  dangerMode: true,
})
.then((willDelete) => {
  if (willDelete) {
    location.href = "/Medico/borrar/" + id;
    swal("Se ha borrado exitosamente!", {
      icon: "success",
    });

  } else {
    swal("la informacion no se va a borrar!");
  }
});
}

(function(){
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmacion = confirm('Esta seguro de remover el Curso?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
    
})();


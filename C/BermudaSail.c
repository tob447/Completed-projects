#include <stdio.h>
/* el operador * se usa para guardar la direccion tambien se usa para sacar el valor de la direccion, el & se usa para 
obtener la direccion en memoria donde esta la variable*/

void go_south_east(int *lat, int *lon){
    *lat=*lat-1;
    *lon=*lon+1;
}


main(){
    int latitude=32;
    int longitude=-64;
    go_south_east(&latitude,&longitude);
    printf("Avast! Now at: [%i,%i]\n",latitude,longitude);
    return 0;
}
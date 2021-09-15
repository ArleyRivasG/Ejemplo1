/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package semana2;

public class Vehiculo {
    public String nombre;
    private int precio;

    public Vehiculo() {
    }
    
    public Vehiculo(String nombre, int precio) {
        this.nombre = nombre;
        this.precio = precio;
    }


    public int getPrecio() {
        return precio;
    }

    public void setPrecio(int precio) {
        this.precio = precio;
    }

    
    
    
}

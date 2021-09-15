/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semana2;

/**
 *
 * @author sistemas
 */
public class PrincipalVehiculo {
    public static void main(String[] args) {
       Vehiculo vehiculo1 = new Vehiculo();
       
       vehiculo1.nombre = "Tesla";
       vehiculo1.setPrecio(1000);
       
       Vehiculo vehiculo2 = new Vehiculo();
       vehiculo2.nombre="Mazda";
       vehiculo2.setPrecio(500);
       
       System.out.println("vehiculo 1, nombre: " + vehiculo1.nombre + " precio: " + vehiculo1.getPrecio());
       System.out.println("vehiculo 2, nombre: " + vehiculo2.nombre + " precio: " + vehiculo2.getPrecio());
    }
    
}

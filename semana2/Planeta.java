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
public class Planeta {
    
    //atributos 
    private String nombre;
    private float masa;
    
//    ctrl + shift + c 
//para comentar las líneas seleccionadas

    //construtores              

    public Planeta() {
        this.masa= 4000;
    }

    public Planeta(String nombre, float masa) {
        this.nombre = nombre;
        this.masa = masa;
    }

    
    //metodos Get and Set
    
    
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public float getMasa() {
        return masa;
    }

    public void setMasa(float masa) {
        this.masa = masa;
    }
    
}

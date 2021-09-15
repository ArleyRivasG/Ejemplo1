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
public class Gafa {
    public String nombre;
    private double precio;
    public static int contador = 0;
    
    //FINAL para hacerla constante 
    //STATIC es un atributo de clase, puedo acceder a el desde la clase sin instanciarla para que no se repita(queda global)
    public static final double IVA = 0.19;
    public static int ENVIO = 2000;

    public Gafa() {
        Gafa.contador = Gafa.contador + 1;
    }

    public Gafa(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
        Gafa.contador = Gafa.contador + 1;
    }

    public double precioConIva() {
    
        double total = this.precio + (this.precio * Gafa.IVA);
        return total;
    }

    public double precioConIvaEnvio() {
        
        double total = this.precio + (this.precio * this.IVA) + this.ENVIO;
        return total;
    }
    public static void imprimirDatos(){
        //no pueeedo usar la palabra this al no atributos de instancia sino de clase
        System.out.println("IVA "+Gafa.IVA);
        System.out.println("ENVIO "+Gafa.ENVIO);
    }

}

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
public class PrincipalCirculo {
    public static void main(String[] args) {
        Circulo circulo1 = new Circulo();
        circulo1.setRadio(5);
        
        Circulo circulo2 =  new Circulo();
        
        Circulo circulo3=  new Circulo(7);
        
        
        //circulo1.radio = 6;  Error atributo privado
        System.out.println("perimetro de radio: " + circulo1.getRadio() + " es: "+circulo1.getPerimetro());
        System.out.println("perimetro de radio: " + circulo2.getRadio() + " es: "+circulo2.getPerimetro());
        System.out.println("perimetro de radio: " + circulo3.getRadio() + " es: "+circulo3.getPerimetro());
    }
    
}

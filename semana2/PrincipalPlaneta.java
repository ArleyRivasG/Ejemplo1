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
public class PrincipalPlaneta {
    public static void main(String[] args) {
        Planeta planeta1 = new Planeta();
        planeta1.setNombre("Jupiter");
        Planeta planeta2 = new Planeta("Venus", 50);
        
        
        //System.out.println("Planeta 1 Masa:" + planeta1.getMasa());
        System.out.println("Planeta 1 Masa:" + planeta1.getMasa()  + " Nombre: " + planeta1.getNombre());        
        System.out.println("Planeta 2 Masa:" + planeta2.getMasa()  + " Nombre: " + planeta2.getNombre());        
        
//        planeta1.nombre="mercurio";
//        System.out.println("Planeta 1 Masa:" + planeta1.getMasa()  + " Nombre: " + planeta1.getNombre());        
        
    }
}

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
public class Circulo {

    private double radio;
    private String name;
    
    
    //contructores
    public Circulo(){    
        this.radio=1;
    }

    public Circulo(double r){    
        this.radio=r;
    }
    
    
    //Metodos
    public double getRadio() {
        return this.radio;
    }

    public void setRadio(double radio) {
        this.radio = radio;
    }
    
    //visibilidad, lo que devuelve y nombre del metodo (parametros)
    public double getPerimetro(){
        return 2 * Math.PI * this.radio;
    }
}


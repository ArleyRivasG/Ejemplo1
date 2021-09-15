/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semana2;

/**
 *
 * @author recepcionopp
 */
public class PointStatic {
    public static int x1;
    public static int y1;
    public static int x2;
    public static int y2;
    private double minX;
    private double minY;

//    public PointStatic() {
//    }
    public PointStatic() {
    }

    public PointStatic(double x, double y) {
        this.minX = x;
        this.minY = y;
    }

    public static int getX1() {
        return x1;
    }

    public static void setX1(int x1) {
        PointStatic.x1 = x1;
    }

    public static int getY1() {
        return y1;
    }

    public static void setY1(int y1) {
        PointStatic.y1 = y1;
    }

    public static int getX2() {
        return x2;
    }

    public static void setX2(int x2) {
        PointStatic.x2 = x2;
    }

    public static int getY2() {
        return y2;
    }

    public static void setY2(int y2) {
        PointStatic.y2 = y2;
    }

    public double getMinX() {
        return minX;
    }

    public void setMinX(double minX) {
        this.minX = minX;
    }

    public double getMinY() {
        return minY;
    }

    public void setMinY(double minY) {
        this.minY = minY;
    }
   
    
    public static void puntoMedio() {

        double midX = ((PointStatic.getX1() + PointStatic.getX2()) / 2);
        double midY = ((PointStatic.getY1() + PointStatic.getY2()) / 2);
        System.out.println("el punto medio entre x1=" + PointStatic.getX1() + " x2="
                + PointStatic.getX2() + ", y1=" + PointStatic.getY1() + " y2=" + PointStatic.getY2()+ " es X:" + midX + ", Y:" + midY);
    }
    
     public static PointStatic puntoMedio2() {
        
        double midX = ((PointStatic.x1 + PointStatic.x2) / 2);
        double midY = ((PointStatic.y1 + PointStatic.y2) / 2);
        
        PointStatic puntMed = new PointStatic(midX, midY);
        System.out.println("el punto medio entre x1=" + PointStatic.x1 + " x2="
                + PointStatic.x2 + ", y1=" + PointStatic.y1 + " y2=" + PointStatic.y2 + " es X:" + puntMed.minX + ", Y:" + puntMed.minY);

        return puntMed;
    }


    
    public static void main(String[] args) {
        
        PointStatic.setX1(2);
        PointStatic.setY1(1);
        PointStatic.setX2(4);
        PointStatic.setY2(3);
      
        PointStatic.puntoMedio();
        
        
        PointStatic pm = new PointStatic();
        pm = PointStatic.puntoMedio2();
        
        System.out.println("punto medio X = " + pm.minX + " Punto medio Y = " + pm.minY);
        
        
    }
}



/*
descarga Nod32 antivirus y activa el trial por 30 días 
con un correo y actívalo para qu ete elimine todo

 */
package semana2;

public class Point {

    private double x;
    private double y;

    //1
    public Point() {
        this.x = 0;
        this.y = 0;
    }
    public Point(Point p) {
           this(p.getX(), p.getY());
          
       }
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    

    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    public void setX(double x) {
        this.x = x;;
    }

    public void setY(double y) {
        this.y = y;
    }

    @Override //sobreescribimo el metodos toString()
    public String toString() {
        return "Point{" + "x=" + this.x + ", y=" + this.y + '}';
    }

    
    
    
    public double distance(double x, double y) {
        double dist = Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2));
        System.out.println("me fui por el double: ");
        return dist;
    }

    public double distance(int x, int y) {
        double dist = Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2));
        System.out.println("me fui por el int: ");
        return dist;

    }

    public double distance(Point p) {
        double dist = Math.sqrt(Math.pow(this.x - p.getX(), 2) + Math.pow(this.y - p.getY(), 2));
        return dist;
    }
    
    

    public Point puntoMedio(Point p) {

        double midX = ((this.x + p.getX()) / 2);
        double midY = ((this.y + p.getY()) / 2);
        Point puntoMedio = new Point(midX, midY);
        return puntoMedio;

    }
    
    public static Point StaticPuntoMedio(Point p1, Point p2) {

        double midX = ((p1.x + p2.getX()) / 2);
        double midY = ((p1.y + p2.getY()) / 2);
        Point puntoMedio = new Point(midX, midY);
        return puntoMedio;

    }
    

    public static void main(String[] args) {

        Point punto1 = new Point(2, 1);
        Point punto2 = new Point(4, 3);

        double distancia1 = 0;
        distancia1 = punto1.distance(punto2.getX(), punto2.getY());
        System.out.println(distancia1);

        double distancia2 = 0;
        distancia2 = punto1.distance(punto2);

        System.out.println(distancia2);

        double distancia3 = 0;
        distancia3 = punto2.distance(punto1);
        System.out.println(distancia3);
        double distancia4 = 0;
        int x = 2;
        double y = 3.4;
        distancia4 = punto1.distance(x, y);
        System.out.println(distancia4);

        //hallar el punto medio entre punto1 y punto2
        Point puntoMedio = punto1.puntoMedio(punto2);
        System.out.println("El punto medio en X es: " + puntoMedio.getX() + " El punto medio en Y es: " + puntoMedio.getY());
        System.out.println("metodo toString(): " + puntoMedio.toString());
   
        Point pMedSta = new Point();
        pMedSta = Point.StaticPuntoMedio(punto1, punto2);
        System.out.println("El punto medio en X es: " + pMedSta.getX() + " El punto medio en Y es: " + pMedSta.getY());
        
        pMedSta.toString();
        
    }
}

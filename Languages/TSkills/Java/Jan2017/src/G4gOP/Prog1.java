/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package G4gOP;

/**
 *
 * @author esoussh
 */
class Test{
    protected int x=10; protected float y=10;
}
public class Prog1 {
    public static void main(String[] args) {
        Test t=new Test();
        t.x=20;
        System.out.println(t.x+" "+t.y);
    }
}

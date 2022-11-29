import  java.util.*;
class A {
    String getf(){return "97.3";}
    static String getf2(){return "97.3";}
}
public class B extends A {
    String getf(){return "50.1";}
    static String getf2(){return "50.1";}
    public static void main(String[] args){
        List<A> rs = new ArrayList<A>();
        rs.add(new A());
        rs.add(new B());
        for(A r:rs){
            System.out.print(r.getf()+" "+r.getf2());
        }

    }

}

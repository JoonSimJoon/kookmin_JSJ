public class Boot {
    static  String s;
    static  {s="";}
    {
        System.out.print("shiner");
    }
    static {
        System.out.print(s.concat("better"));
    }
    Boot(){
        System.out.print(s.concat("bigger"));
    }
    public static void main(String[] ags){
        new Boot();
        System.out.print("boot");
    }
}

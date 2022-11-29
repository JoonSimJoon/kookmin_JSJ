
public class C{
    public int cnt;

    public void o(int a){
        while(a>1){
            for(int i=2;i<a;i++){
                if(a%i==0){
                    cnt++;
                    a/=i;
                }
            }
        }
    }
    public static  void main(String[] args){
        o(100);
        System.out.print(cnt);
    }
}

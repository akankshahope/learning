import java.io.BufferedReader;
import java.io.InputStreamReader;
/*Making the pattern as Z*/
class TestClass {
    public static void main(String args[] ) throws Exception {
       
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);
        if(N>2 && N<=20){
        	int last=N-1;
        	int temp=N;
        	for(int i=0;i<=last;i++){
        		if(i==0||i==last){
        			temp=N;
        			while(temp>0){
        				System.out.print("*");
        				temp--;
        			}
        			System.out.println();
        		}else{
        			int temp2=N-i-1;
        			while(temp2>0){
        				System.out.print(" ");
        				temp2--;
        			}
        			System.out.print("*");
        			System.out.println();
        		}
        	}
        }
    }
}


import java.util.Arrays;

public class CopyArrayUsingThread implements Runnable{

	@Override
	public void run() {
		int[] i = {1,2,3,4};
		int[] temp = new int[i.length];
		for(int j=0;j< i.length;j++){
			 temp[j] = i[j];
		}
		System.out.println(Arrays.toString(temp));
	}
	
	public static void main(String[] abd) throws InterruptedException {
		Thread t1 = new Thread(new CopyArrayUsingThread());
		
		t1.start();
		t1.join();
		
	}

}

import java.util.ArrayList;


public class CustomAdapterThreadWrapper extends Thread
{
	public static CustomAdapter adapter;
	
	
	public CustomAdapterThreadWrapper(ArrayList<Drink> drinks)
	{
		adapter = new CustomAdapter(drinks);
	}
	
	//EDMUND:
	public void run()
	{
		
	}
}
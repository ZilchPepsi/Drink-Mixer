package greenbrier.drinkmixer3000;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.widget.LinearLayout;

/**
 * Created by McGiv on 8/31/2017.
 */

public class MainActivity extends AppCompatActivity
{
    private Network net;
    private static int pin;

    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        RecyclerView recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this, LinearLayout.VERTICAL,false));

        CustomAdapter adapter = new CustomAdapter();
        recyclerView.setAdapter(adapter);

        if(isNetworkConnected())
        {
            net = new Network(adapter);
            net.execute("init");
        }
        else
        {
            Log.d("Network", "Network not connected");
        }
    }

    public static void setPin(int pin)
    {
        MainActivity.pin = pin;
    }


    private boolean isNetworkConnected()
    {
        ConnectivityManager connMgr = (ConnectivityManager)
        getSystemService(Context.CONNECTIVITY_SERVICE); // 1
        NetworkInfo networkInfo = connMgr.getActiveNetworkInfo(); // 2
        return networkInfo != null && networkInfo.isConnected(); // 3
    }
}

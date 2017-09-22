package greenbrier.drinkmixer3000;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Debug;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.Toast;

import java.util.ArrayList;

/**
 * Created by McGiv on 8/31/2017.
 */

public class MainActivity extends AppCompatActivity
{
    public static final String DRINKS_PARCELABLE_NAME = "MIX_N_DRINKS";

    private Network net;
    private static int pin;
    private ArrayList<Drink> drinks;
    private ArrayList<Mix> mixes;

    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        drinks = new ArrayList<Drink>();
        mixes = new ArrayList<Mix>();


        if(isNetworkConnected())
        {
            net = new Network();
            net.execute(new WorkOrder(Network.INIT, mixes, drinks));
        }
        else
        {
            Log.d("Network", "Network not connected");
        }

    }

    @Override
    public void onStart()
    {
        super.onStart();
    }

    @Override
    public void onSaveInstanceState(Bundle savedInstanceState)
    {
        super.onSaveInstanceState(savedInstanceState);

        Log.d("instances", "save instance called");

        savedInstanceState.putInt("PIN", pin);
        savedInstanceState.putParcelable(DRINKS_PARCELABLE_NAME, new DrinksParcelable(drinks,mixes));
    }
    @Override
    public void onRestoreInstanceState(Bundle savedInstanceState)
    {
        super.onRestoreInstanceState(savedInstanceState);

        Log.d("instances", "restore instance called");

        pin = savedInstanceState.getInt("PIN");
        DrinksParcelable dp = savedInstanceState.getParcelable(DRINKS_PARCELABLE_NAME);
        drinks = dp.drinks;
        mixes = dp.mixes;
    }




    public void gotoMixView(View view)
    {

        if(net.getStatus() == AsyncTask.Status.RUNNING)
        {
            Toast.makeText(getApplicationContext(), "wait for initialization", Toast.LENGTH_SHORT).show();

        }
        else
        {
            Intent intent = new Intent(this, MakeMixViewActivity.class);
            intent.putExtra(DRINKS_PARCELABLE_NAME, new DrinksParcelable(drinks, mixes));
            startActivity(intent);
        }
    }

    public void gotoSettingsView(View view)
    {
        //TODO go to settings view
    }

    public boolean isNetworkConnected()
    {
        ConnectivityManager connMgr = (ConnectivityManager)
                getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
        return networkInfo != null && networkInfo.isConnected();
    }

    public static void setPin(int pin)
    {
        MainActivity.pin = pin;
    }
    public static int getPin()
    {
        return pin;
    }

}

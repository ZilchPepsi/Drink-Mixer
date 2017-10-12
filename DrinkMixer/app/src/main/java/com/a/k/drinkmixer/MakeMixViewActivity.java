package com.a.k.drinkmixer;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by McGiv on 8/31/2017.
 */

public class MakeMixViewActivity extends AppCompatActivity
{
    private ArrayList<Mix> mixes;


    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_make_mix_view);

        //Log.d("ActivityState", "onCreate");

        RecyclerView recyclerView = (RecyclerView) findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this, LinearLayout.VERTICAL,false));

        DrinksParcelable dp = getIntent().getParcelableExtra(MainActivity.DRINKS_PARCELABLE_NAME);
        MakeMixAdapter adapter = new MakeMixAdapter(dp.drinks,dp.mixes);
        mixes = dp.mixes;
        recyclerView.setAdapter(adapter);
    }

    public int findMix(String name)
    {
        for(int x= 0; x<mixes.size(); x++)
            if(mixes.get(x).getName().equals(name))
                return x;
        return -1;
    }


    public void clickedDrink(View view)
    {
        String drinkName = ((TextView)((ViewGroup) view).getChildAt(0)).getText().toString();
        int pos = findMix(drinkName);
        if(pos!=-1)
            new Network().execute(new WorkOrder(Network.MAKE_MIX, pos));
        else
            Log.d("Network", "tried to send drink pos -1");
    }



    @Override
    public void onStart()
    {
        super.onStart();
      //  Log.d("ActivityState", "onStart");
    }
    @Override
    public void onRestart()
    {
        super.onRestart();
      //  Log.d("ActivityState", "onRestart");
    }
    @Override
    public void onPause()
    {
        super.onPause();
      //  Log.d("ActivityState", "onPause");
    }
    @Override
    public void onResume()
    {
        super.onResume();
       // Log.d("ActivityState", "onResume");
    }
    @Override
    public void onStop()
    {
        super.onStop();
      // Log.d("ActivityState", "onStop");
    }
    @Override
    public void onDestroy()
    {
        super.onDestroy();
      //  Log.d("ActivityState", "onDestroy");
    }
}

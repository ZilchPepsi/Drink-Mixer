package com.a.k.drinkmixer;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

public class SetDrinksActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_set_drinks);

        //TODO add recycler view
        RecyclerView recyclerView = (RecyclerView) findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false));

        DrinksParcelable dp = getIntent().getParcelableExtra(MainActivity.DRINKS_PARCELABLE_NAME);
        Settings_DrinkAdapter adapter = new Settings_DrinkAdapter(dp.drinks);
        recyclerView.setAdapter(adapter);

    }


    public void addDrink (View v)
    {
        Toast.makeText(getApplicationContext(), "Pressed button", Toast.LENGTH_SHORT).show();
        Log.d("editButton", "I got pressed");
    }
}

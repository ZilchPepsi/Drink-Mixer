package greenbrier.drinkmixer3000;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import java.util.ArrayList;

public class SettingsActivity extends AppCompatActivity {

    private DrinksParcelable dp;


    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        dp = getIntent().getParcelableExtra(MainActivity.DRINKS_PARCELABLE_NAME);
    }

    @Override
    public void onBackPressed()
    {
        Intent intent = new Intent(this, MainActivity.class);

        intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);

        startActivity(intent);
    }

    public void setDrinks(View view)
    {
        //TODO go to set drinks screen
        Intent intent = new Intent(this, SetDrinksActivity.class);
        intent.putExtra(MainActivity.DRINKS_PARCELABLE_NAME, dp);
        startActivity(intent);
    }
    public void setMixes(View view)
    {
        //TODO go to set mixes Screen
    }
    public void setPin(View view)
    {
        //TODO go to set pin screen
    }



}

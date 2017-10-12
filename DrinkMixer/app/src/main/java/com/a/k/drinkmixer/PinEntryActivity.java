package com.a.k.drinkmixer;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class PinEntryActivity extends AppCompatActivity {

    private int inputCount;
    private TextView input;
    private DrinksParcelable dp;


    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pin_entry);
        input = (TextView) findViewById(R.id.pin_input);
        inputCount = 0;

        dp = getIntent().getParcelableExtra(MainActivity.DRINKS_PARCELABLE_NAME);
    }

    public void numPressed(View view)
    {
        switch(view.getId())
        {
            case R.id.pin_0:
                input.append("0");
                inputCount++;
                break;
            case R.id.pin_1:
                input.append("1");
                inputCount++;
                break;
            case R.id.pin_2:
                input.append("2");
                inputCount++;
                break;
            case R.id.pin_3:
                input.append("3");
                inputCount++;
                break;
            case R.id.pin_4:
                input.append("4");
                inputCount++;
                break;
            case R.id.pin_5:
                input.append("5");
                inputCount++;
                break;
            case R.id.pin_6:
                input.append("6");
                inputCount++;
                break;
            case R.id.pin_7:
                input.append("7");
                inputCount++;
                break;
            case R.id.pin_8:
                input.append("8");
                inputCount++;
                break;
            case R.id.pin_9:
                input.append("9");
                inputCount++;
                break;
            case R.id.pin_clear:
                input.setText("");
                inputCount = 0;
                break;
        }

        if(inputCount == 4)
        {
            Log.d("pinEntry", "about to parse");

            int userPin = Integer.parseInt(input.getText().toString());
            Log.d("pinEntry", "parsed");
            if(userPin == MainActivity.getPin())
            {
                Intent intent = new Intent(this, SettingsActivity.class);
                intent.putExtra(MainActivity.DRINKS_PARCELABLE_NAME, dp);
                startActivity(intent);
            }
            else
            {
                input.setText("");
                inputCount = 0;
                Toast.makeText(this, "Invalid pin", Toast.LENGTH_SHORT).show();
            }
        }
    }






}

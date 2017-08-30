package greenbrier.drinkmixer3000;

import android.app.Activity;
import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;

import android.os.AsyncTask;

import android.util.Log;

import java.io.IOException;
import java.net.Socket;

/**
 * Created by McGiv on 8/29/2017.
 */

public class Network extends AsyncTask<String, Integer , String>
{
    public static final String SERVER_IP = "192.168.0.30";
    public static final int SERVER_PORT = 1234;

    Socket socket;


    public Network()
    {

    }

    @Override
    protected void onPreExecute()
    {
        Log.d("Async","I am on preExecute! "+Thread.currentThread().getId());
    }


    @Override
    protected String doInBackground(String... params)
    {
        Log.d("Async","I am working! "+Thread.currentThread().getId());
        //can call publishProgress() here


        switch(params[0])
        {
            case "init":
                try
                {
                    socket = new Socket(SERVER_IP, SERVER_PORT);
                }
                catch(IOException e)
                {
                    Log.d("Network","Could not connect to server");
                }
                break;
            default:
                break;
        }
        return null;
    }

    @Override
    protected void onProgressUpdate(Integer... progress)
    {
        Log.d("Async", "I did some updating! "+Thread.currentThread().getId());
    }



    @Override
    protected void onPostExecute(String result)
    {
        Log.d("Async", "I am done! "+Thread.currentThread().getId());
    }
}

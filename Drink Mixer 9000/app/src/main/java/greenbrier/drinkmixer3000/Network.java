package greenbrier.drinkmixer3000;

import android.app.Activity;
import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;

import java.io.InputStream;

import android.os.AsyncTask;

import android.os.Parcel;
import android.os.Parcelable;
import android.support.v7.widget.RecyclerView;
import android.util.Log;

import java.io.IOException;
import java.net.Socket;
import java.util.ArrayList;

/**
 * Created by McGiv on 8/29/2017.
 */

public class Network extends AsyncTask<WorkOrder, Integer , Integer>/*params, progress, result*/
{


    public static final String SERVER_IP = "192.168.0.30";//TODO if grabbing static IP then won't work on other networks
    public static final int SERVER_PORT = 1234;

   /*
    bit masks
    */
    public static final byte MAKE_MIX = 0;
    public static final byte ADD_MIX = 1;
    public static final byte MODIFY_MIX = 2;
    public static final byte DELETE_MIX = 3;

    public static final byte ADD_DRINK = 4;
    public static final byte DELETE_DRINK = 5;

    public static final byte INIT = 6;
    public static final byte INIT_CONFIRM = 8;

    public static final byte HELLO = 9;
    public static final byte GOODBYE = 10;
    /*
    END bit masks
     */

    private Socket socket;

    public Network()
    {
    }

    @Override
    protected void onPreExecute()
    {
        Log.d("Async","I am on preExecute! "+Thread.currentThread().getId());//calling thread
    }


    @Override
    protected Integer doInBackground(WorkOrder... params)
    {
        Log.d("Async","I am working! "+Thread.currentThread().getId());//working thread
        //can call publishProgress() here

        switch(params[0].order)
        {
            case INIT:    init(params[0]);
                break;
            case MAKE_MIX : makeMix(params[0]);

        }
        return params[0].order;
    }

    private boolean connect()
    {
        Log.d("Network","starting network connection");
        int attempts = 0;
        while(attempts< 3)
        {
            try
            {
                socket = new Socket(SERVER_IP, SERVER_PORT);
                break;
            }
            catch (IOException e)
            {
                Log.d("Network", "Could not connect to server, attempt" + attempts);
                attempts++;
            }
        }
        if(!socket.isConnected())
        {
            Log.d("Network", "I'm not connected, cancelling");
            try
            {
                socket.close();
            } catch (IOException e)
            {
                Log.d("Network", "Could not close socket");
            }
            return false;
        }
        return true;
    }



    private void makeMix(WorkOrder workOrder)
    {
        int drinkNum = ((Integer)workOrder.data.get(0));

        if(!connect())
        {
            cancel(true);
        }

        try
        {
            Log.d("Network", "sending makeMix..."+MAKE_MIX);
            socket.getOutputStream().write(new byte[]{MAKE_MIX, (byte)drinkNum});
            socket.getOutputStream().flush();
        }
        catch(IOException e) {}
        try {
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    /**
     * creates socket
     * connects to server
     * receives and interprets pin, drinks, and mixes
     *
     * data:
     * ArrayList<Mix>
     * ArrayList<Drink>
     */
    private void init(WorkOrder workOrder)
    {
        ArrayList<Mix> mixes = (ArrayList<Mix>) workOrder.data.get(0);
        ArrayList<Drink> drinks = (ArrayList<Drink>) workOrder.data.get(1);


        if(!connect())
        {
            cancel(true);
        }


        try
        {
            Log.d("Network", "sending hello..."+HELLO);
            socket.getOutputStream().write(new byte[]{HELLO});
            socket.getOutputStream().flush();
        }
        catch(IOException e) {}

        //getting startup data
        InputStream in = null;
        try
        {
            in = socket.getInputStream();
        }
        catch (IOException e)
        {

        }
        try
        {
            Log.d("Network", "waiting for init string");
            while(in.available() ==0)
                    try
                    {
                        Thread.sleep(50);
                    }
                    catch(InterruptedException e)
                    {

                    }
        }
        catch (IOException e)
        {

        }

        byte[] initStuff = null;
        try
        {
            initStuff = new byte[in.available()];
            in.read(initStuff);
        }
        catch(IOException e)
        {

        }

        String initS = "";
        for( int x= 0; x< initStuff.length; x++)
        {
            initS += (char)initStuff[x];
        }

        String[] s = initS.split(":");


        if(s[0].equals(""+INIT))
        {
            MainActivity.setPin(Integer.parseInt(s[1]));
        }
        int drinkCount = Integer.parseInt(s[2]);
        int pos = 3;
        for(; pos< drinkCount*2+3;  pos+=2)
        {
            drinks.add(new Drink(s[pos], Boolean.parseBoolean(s[pos+1])));
        }

        int numMixes = Integer.parseInt(s[pos]);
        pos++;

        for(int x =0; x< numMixes; x++)
        {

            Mix m = new Mix(s[pos]);
            pos++;
            drinkCount = Integer.parseInt(s[pos]);
            pos++;
            for (int y = 0; y < drinkCount; y++)
            {
                Drink d = findDrink(drinks, s[pos]);
                if (d != null)
                {
                    m.addDrink(d, Integer.parseInt(s[pos + 1]));
                }
                pos += 2;
            }

            mixes.add(m);
        }

        Log.d("Network", "finished init, shutting down socket");
        Log.d("ActivityState", "finished init, shutting down socket");

        try
        {
            socket.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    private Drink findDrink(ArrayList<Drink> drinks, String name)
    {
        for(int x =0; x< drinks.size(); x++)
            if(drinks.get(x).name.equals(name))
                return drinks.get(x);
        return null;
    }





    @Override
    protected void onProgressUpdate(Integer... progress)
    {
        Log.d("Async", "I did some updating! "+Thread.currentThread().getId());
    }



    @Override
    protected void onPostExecute(Integer result)
    {
    }

    @Override
    protected void onCancelled(Integer result)
    {
        Log.d("Network", "I got cancelled");

    }


}

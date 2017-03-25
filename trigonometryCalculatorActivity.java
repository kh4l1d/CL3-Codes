package com.example.khalid.trigocalc;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;


import android.view.View; // need to add this separately

    public class CalcActivity extends AppCompatActivity
{
    // global stuff here
    TextView result;
    String currentNumber = "";
    double answer = 0;

    void numberPressed(int n)
    {
        currentNumber += String.valueOf(n);
        result.setText(currentNumber);
    }

    public enum Operation
    {
        SIN,COS,TAN,EQUALS
    }

    void processOperation(Operation operation)
    {
        if(currentNumber != null)
        {
            switch (operation)
            {
                case SIN :
                    answer = Math.sin(Math.toRadians(Integer.parseInt(currentNumber)));
                    break;

                case COS :
                    answer = Math.cos(Math.toRadians(Integer.parseInt(currentNumber)));
                    break;

                case TAN :
                    answer = Math.tan(Math.toRadians(Integer.parseInt(currentNumber)));
                    break;

                case EQUALS :
                    result.setText(String.valueOf(answer));
                    break;
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calc);

        Button zero = (Button)findViewById(R.id.zero);
        Button one = (Button)findViewById(R.id.one);
        Button two = (Button)findViewById(R.id.two);
        Button three = (Button)findViewById(R.id.three);
        Button four = (Button)findViewById(R.id.four);
        Button five = (Button)findViewById(R.id.five);
        Button six = (Button)findViewById(R.id.six);
        Button seven = (Button)findViewById(R.id.seven);
        Button eight = (Button)findViewById(R.id.eight);
        Button nine = (Button)findViewById(R.id.nine);
        Button equals = (Button)findViewById(R.id.equals);
        Button clear = (Button)findViewById(R.id.clear);
        final Button sin = (Button)findViewById(R.id.sin);
        final Button cos = (Button)findViewById(R.id.cos);
        final Button tan = (Button)findViewById(R.id.tan);
        result = (TextView)findViewById(R.id.result);

        result.setText("");

        zero.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(0);
            }
        });

        one.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(1);
            }
        });

        two.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(2);
            }
        });

        three.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(3);
            }
        });

        four.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(4);
            }
        });

        five.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(5);
            }
        });

        six.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(6);
            }
        });

        seven.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(7);
            }
        });

        eight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(8);
            }
        });

        nine.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(9);
            }
        });

        equals.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sin.setBackgroundColor(Color.parseColor("#ffffffff"));
                cos.setBackgroundColor(Color.parseColor("#ffffffff"));
                tan.setBackgroundColor(Color.parseColor("#ffffffff"));
                processOperation(Operation.EQUALS);
            }
        });

        sin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sin.setBackgroundColor(Color.parseColor("#ff33b5e5"));
                processOperation(Operation.SIN);
            }
        });

        cos.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cos.setBackgroundColor(Color.parseColor("#ff33b5e5"));
                processOperation(Operation.COS);
            }
        });

        tan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tan.setBackgroundColor(Color.parseColor("#ff33b5e5"));
                processOperation(Operation.TAN);
            }
        });

        clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                answer = 0;
                currentNumber = "";
                result.setText("0");
            }
        });

    }
}

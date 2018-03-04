# Example 3 app: Running functions to collect data and reading data into templates  

This app differs from the Example 2 app in a huge way: Each route calls a new function that reads data from an external file, *data.py*.

This Flask app is explained in the README in [flask/part3_templates](https://github.com/macloo/python-beginners/tree/master/flask/part3_templates).

To run it (assuming you have Flask installed):

```bash
python students4.py
```

The files *function1_test.py* and *function2_test.py* were each used to refine and test the functions that were added to *students3.py*, which was then run and tested until it all worked. After that, *students4.py* was created, with the only change being to import the dataset from *data.py*.

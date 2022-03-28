LAB
===

.. toctree::
    :hidden:
    :maxdepth: 1
    :caption: LAB

    LAB01.ipynb
    LAB02.ipynb
    Pre_LAB03.ipynb
    Pre_LAB04.ipynb
    Pre_LAB05.ipynb
    Pre_LAB06.ipynb
    Pre_LAB07.ipynb
    Pre_LAB07s.ipynb
    Pre_LAB08.ipynb
    Pre_LAB09.ipynb
    Pre_LAB09.5.ipynb
    Pre_LAB10.ipynb
    Pre_LAB11.ipynb
    Pre_LAB12.ipynb

.. code:: c

    #include <stdio.h>
    #include <stdlib.h>

    static int exit_status;

    int main(int argc, char **argv)
    {
        int ok = 0;

        if (argc > 1)
        {
            ok = 1;
        }
        else
        {
            ok = 0;
        }

        return exit_status = ok ? EXIT_SUCCESS
                                : EXIT_FAILURE;
    }

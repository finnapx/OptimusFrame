import matplotlib.pyplot as plt

tabla = {
    'head': [
        ['fila', 'perfil', 'combo', 'nodo', 'axial', 'corte', 'momento'],
        ['[kg]', '[kg]', '[kg-m]']
    ],
    'body': [
        ['COL', 1, '1.4 D', 'i', 2409.32, -1075.57, -340.37440000000004],
        [                   'j', 2094.32, -1075.57, 735.1998],
        ['COL', 1, '1.2 D + L', 'i', 3459.72, -1638.14, -518.4021],
        [                   'j', 3189.72, -1638.14, 1119.7349000000002],
        ['COL', 1, '1.2 D + 1.6 L', 'i', 4296.48, -2067.87, -654.3937000000001],
        [                   'j', 4026.48, -2067.87, 1413.4731],
        ['COL', 1, '1.2 D + 1.4 E + L', 'i', 2524.45, 1768.9, 1485.7219],
        [                   'j', 2254.45, 1768.9, -283.1811],
        ['COL', 1, '1.2 D - 1.4 E + L', 'i', 4395.0, -5045.18, -2522.5261],
        [                   'j', 4125.0, -5045.18, 2522.6509],
        ['COL', 1, '0.9 D + 1.4 E', 'i', 613.57, 2715.6, 1785.3118],
        [                   'j', 411.07, 2715.6, -930.2876],
        ['COL', 1, '0.9 D - 1.4 E', 'i', 2484.13, -4098.48, -2222.9361],
        [                   'j', 2281.63, -4098.48, 1875.5445000000002],
        ['COL', 2, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 2, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 2, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 2, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 2, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 2, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 2, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 3, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 3, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 3, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 3, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 3, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 3, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 3, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 4, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 4, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 4, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 4, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 4, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 4, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 4, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 5, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 5, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 5, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 5, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 5, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 5, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 5, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 6, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 6, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 6, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 6, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 6, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 6, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 6, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 7, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 7, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 7, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 7, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 7, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 7, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 7, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 8, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 8, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 8, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 8, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 8, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 8, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 8, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 9, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 9, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 9, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 9, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 9, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 9, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 9, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 10, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 10, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 10, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 10, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 10, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 10, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 10, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 11, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 11, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 11, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 11, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 11, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 11, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 11, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['COL', 12, '1.4 D', 'i', 2409.32, 1075.57, 340.37440000000004],
        [                   'j', 2094.32, 1075.57, -735.1998],
        ['COL', 12, '1.2 D + L', 'i', 3459.72, 1638.14, 518.4021],
        [                   'j', 3189.72, 1638.14, -1119.7349000000002],
        ['COL', 12, '1.2 D + 1.6 L', 'i', 4296.48, 2067.87, 654.3937000000001],
        [                   'j', 4026.48, 2067.87, -1413.4731],
        ['COL', 12, '1.2 D + 1.4 E + L', 'i', 4395.0, 5045.18, 2522.5261],
        [                   'j', 4125.0, 5045.18, -2522.6509],
        ['COL', 12, '1.2 D - 1.4 E + L', 'i', 2524.45, -1768.9, -1485.7219],
        [                   'j', 2254.45, -1768.9, 283.1811],
        ['COL', 12, '0.9 D + 1.4 E', 'i', 2484.13, 4098.48, 2222.9361],
        [                   'j', 2281.63, 4098.48, -1875.5445000000002],
        ['COL', 12, '0.9 D - 1.4 E', 'i', 613.57, -2715.6, -1785.3118],
        [                   'j', 411.07, -2715.6, 930.2876],
        ['VIGA', 13, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 13, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 13, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 13, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 13, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 13, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 13, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
        ['VIGA', 14, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 14, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 14, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 14, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 14, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 14, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 14, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
        ['VIGA', 15, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 15, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 15, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 15, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 15, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 15, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 15, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
        ['VIGA', 16, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 16, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 16, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 16, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 16, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 16, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 16, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
        ['VIGA', 17, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 17, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 17, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 17, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 17, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 17, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 17, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
        ['VIGA', 18, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 18, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 18, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 18, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 18, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 18, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 18, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
        ['VIGA', 19, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 19, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 19, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 19, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 19, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 19, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 19, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
        ['VIGA', 20, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 20, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 20, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 20, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 20, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 20, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 20, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
        ['VIGA', 21, '1.4 D', 'i', 1075.57, 2094.32, 735.1998],
        [                   'j', 1075.57, -2094.32, 735.1998],
        ['VIGA', 21, '1.2 D + L', 'i', 1638.14, 3189.72, 1119.7349000000002],
        [                   'j', 1638.14, -3189.72, 1119.7349000000002],
        ['VIGA', 21, '1.2 D + 1.6 L', 'i', 2067.87, 4026.48, 1413.4731],
        [                   'j', 2067.87, -4026.48, 1413.4731],
        ['VIGA', 21, '1.2 D + 1.4 E + L', 'i', 1638.14, 2254.45, -283.1811],
        [                   'j', 1638.14, -4125.0, 2522.6509],
        ['VIGA', 21, '1.2 D - 1.4 E + L', 'i', 1638.14, 4125.0, 2522.6509],
        [                   'j', 1638.14, -2254.45, -283.1811],
        ['VIGA', 21, '0.9 D + 1.4 E', 'i', 691.44, 411.07, -930.2876],
        [                   'j', 691.44, -2281.63, 1875.5445000000002],
        ['VIGA', 21, '0.9 D - 1.4 E', 'i', 691.44, 2281.63, 1875.5445000000002],
        [                   'j', 691.44, -411.07, -930.2876],
    ]
}

def filtroCV(combis, combi_e, combi_s, tab, largosV, largosC):
    bars1=[[tab[i-1]+tab[i] for j in range(2) if j==1]
            for i in range(len(tab)) if i%2!=0]
    bars2=[bars1[i][0] for i in range(len(bars1))]
    bars=[[bars2[i] for i in range(combis*j, combis*j+combis)]
            for j in range(int(len(bars2)/combis))]
    bars_e1=[bars2[i] for i in range(len(bars2)) if 'E' in bars2[i][2]]
    bars_s1=[bars2[i] for i in range(len(bars2)) if 'E' not in bars2[i][2]]
    bars_e=[[bars_e1[i] for i in range(combi_e*j, combi_e*j+combi_e)]
            for j in range(int(len(bars_e1)/combi_e))]
    bars_s=[[bars_s1[i] for i in range(combi_s*j, combi_s*j+combi_s)]
            for j in range(int(len(bars_s1)/combi_s))]
    col_e=[[bars_e[j][i] for i in range(0, combi_e)] for j in range(len(bars_e))
            if bars_e[j][0][0]=='COL']
    col_s=[[bars_s[j][i] for i in range(0, combi_s) if bars_s[j][i][2]!='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='COL']
    col_dl=[[bars_s[j][i] for i in range(0, combi_s) if bars_s[j][i][2]=='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='COL']
    vig_e=[[bars_e[j][i] for i in range(0, combi_e)]
            for j in range(len(bars_e)) if bars_e[j][0][0]=='VIGA']
    vig_s=[[bars_s[j][i] for i in range(0, combi_s)if bars_s[j][i][2]!='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='VIGA']
    vig_dl=[[bars_s[j][i] for i in range(0, combi_s)if bars_s[j][i][2]=='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='VIGA']

    maTrix_ij = lambda lista:[[[round(lista[k][j][i],1) for j in range(len(lista[0]))]
                               for i in [5,9]] for k in range(len(lista))]

    maxTrix_i = lambda lista:[[round(max([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [4,5,6]] for k in range(len(lista))]
    minTrix_i = lambda lista:[[round(min([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [4,5,6]] for k in range(len(lista))]
    maxTrix_j = lambda lista:[[round(max([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [8,9,10]] for k in range(len(lista))]
    minTrix_j = lambda lista:[[round(min([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [8,9,10]] for k in range(len(lista))]

    npisos, nbahias = len(col_e)-len(vig_e), int(len(vig_e)/(len(col_e)-len(vig_e)))

    forma_col = lambda lista, nbahias, npisos:[
        [lista[j] for j in range(i*(nbahias+1), (i+1)*(nbahias+1))] for i in range(npisos)]
    forma_vig = lambda lista, nbahias, npisos:[
        [lista[j] for j in range(i*(nbahias), (i+1)*(nbahias))] for i in range(npisos)]

    max_col_ei = forma_col(maxTrix_i(col_e),nbahias,npisos)
    max_col_si = forma_col(maxTrix_i(col_s),nbahias,npisos)
    max_col_dli = forma_col(maxTrix_i(col_dl),nbahias,npisos)

    min_col_ei = forma_col(minTrix_i(col_e),nbahias,npisos)
    min_col_si = forma_col(minTrix_i(col_s),nbahias,npisos)
    min_col_dli = forma_col(minTrix_i(col_dl),nbahias,npisos)

    max_col_ej = forma_col(maxTrix_j(col_e),nbahias,npisos)
    max_col_sj = forma_col(maxTrix_j(col_s),nbahias,npisos)
    max_col_dlj = forma_col(maxTrix_j(col_dl),nbahias,npisos)

    min_col_ej = forma_col(minTrix_j(col_e),nbahias,npisos)
    min_col_sj = forma_col(minTrix_j(col_s),nbahias,npisos)
    min_col_dlj = forma_col(minTrix_j(col_dl),nbahias,npisos)

    mat_col_e = forma_col(maTrix_ij(col_e),nbahias,npisos)
    mat_col_s = forma_col(maTrix_ij(col_s),nbahias,npisos)

    max_vig_ei = forma_vig(maxTrix_i(vig_e),nbahias,npisos)
    max_vig_si = forma_vig(maxTrix_i(vig_s),nbahias,npisos)
    max_vig_dli = forma_vig(maxTrix_i(vig_dl),nbahias,npisos)

    min_vig_ei = forma_vig(minTrix_i(vig_e),nbahias,npisos)
    min_vig_si = forma_vig(minTrix_i(vig_s),nbahias,npisos)
    min_vig_dli = forma_vig(minTrix_i(vig_dl),nbahias,npisos)

    max_vig_ej = forma_vig(maxTrix_j(vig_e),nbahias,npisos)
    max_vig_sj = forma_vig(maxTrix_j(vig_s),nbahias,npisos)
    max_vig_dlj = forma_vig(maxTrix_j(vig_dl),nbahias,npisos)

    min_vig_ej = forma_vig(minTrix_j(vig_e),nbahias,npisos)
    min_vig_sj = forma_vig(minTrix_j(vig_s),nbahias,npisos)
    min_vig_dlj = forma_vig(minTrix_j(vig_dl),nbahias,npisos)

    mat_vig_e = forma_vig(maTrix_ij(vig_e),nbahias,npisos)
    mat_vig_s = forma_vig(maTrix_ij(vig_s),nbahias,npisos)

    matCorte_col=[mat_col_e,mat_col_s]
    matCorte_vig=[mat_vig_e,mat_vig_s]

    #'axial', 'corte', 'momento'
    listaV=[]
    for i in range(len(max_vig_ei)):
        lista1=[]
        lista2=[]
        for j in range(len(max_vig_ei[i])):
            lista1=[[round(max_vig_si[i][j][1]/1000,2), round(max_vig_ei[i][j][1]/1000,2),
                     round(max(max_vig_ei[i][j][2],max_vig_si[i][j][2])/1000,2),
                     round(min(min_vig_ei[i][j][2],min_vig_si[i][j][2])/1000,2),round(max_vig_dli[i][j][1]/1000,2),
                     largosV[i][j],mat_vig_s[i][j][0],mat_vig_e[i][j][0]],
                    [round(max_vig_sj[i][j][1]/1000,2), round(max_vig_ej[i][j][1]/1000,2),
                     round(max(max_vig_ej[i][j][2],max_vig_sj[i][j][2])/1000,2),
                     round(min(min_vig_ej[i][j][2],min_vig_sj[i][j][2])/1000,2),round(max_vig_dlj[i][j][1]/1000,2),
                     largosV[i][j],mat_vig_s[i][j][1],mat_vig_e[i][j][1]]]
            lista2.append(lista1)
        listaV.append(lista2)
    listaC=[]
    for i in range(len(max_col_ei)):
        lista1=[]
        lista2=[]
        for j in range(len(max_col_ei[i])):
            #[vue, vu, .....]
            lista1=[[round(max(max_col_ei[i][j][0], max_col_si[i][j][0])/1000,2),
                     round(min(min_col_ei[i][j][0], min_col_si[i][j][0])/1000,2), round(max_col_si[i][j][1]/1000,2),
                     round(max_col_ei[i][j][1]/1000,2), round(max(max_col_ei[i][j][2],max_col_si[i][j][2],
                                              abs(min_col_ei[i][j][2]),abs(min_col_si[i][j][2]))/1000,2),
                     round(max_col_dli[i][j][1]/1000,2), largosC[i][j],mat_col_s[i][j][0],mat_col_e[i][j][0]],
                    [round(max(max_col_ej[i][j][0], max_col_sj[i][j][0])/1000,2), round(max_col_sj[i][j][1]/1000,2),
                     round(max_col_ej[i][j][1]/1000,2), round(max(max_col_ej[i][j][2],max_col_sj[i][j][2],
                                              abs(min_col_ej[i][j][2]),abs(min_col_sj[i][j][2]))/1000,2),
                     round(max_col_dlj[i][j][1]/1000,2), largosC[i][j],mat_col_s[i][j][1],mat_col_e[i][j][1]]]
            lista2.append(lista1)
        listaC.append(lista2)
    # listaVmax=[[[max(i[j][0][k], i[j][1][k]) for k in range(len(i[j][0]))] for j in range(len(i))] for i in listaV]
    # listaCmax=[[[max(i[j][0][k], i[j][1][k]) for k in range(len(i[j][0]))] for j in range(len(i))] for i in listaC]
    # return [listaV,listaVmax, listaC, listaCmax]
    return [listaV, listaC]

# print(filtroCV(combis, combi_e, combi_s, tab, largosV, largosC))

def V2vig(x1, lo, vuLsti, vueLsti, vuLstj, vueLstj, vupr, vc, state):
    vc = vc if state==1 else 0
    v2Calc = lambda v1, v2, x1, lo: round(v1 - x1 * (v1 - v2) / lo, 1)
    vupr2 = v2Calc(vupr,-vupr,x1,lo)/0.75-vc
    vu2 = max([v2Calc(vuLsti[i],vuLstj[i], x1, lo) for i in range(len(vuLsti))])/0.75-vc
    vue2 = max([v2Calc(vueLsti[i],vueLstj[i], x1, lo) for i in range(len(vueLsti))])/0.6
    return round(max(vupr2,vu2, vue2),1)

def b1(fc):
    if 550 >= fc >= 280:
        return round(0.85-0.05/70*(fc-280), 2)
    else:
        return 0.85 if fc < 280 else 0.65

def et(h,eu,dp,c): return round(eu*abs(h-dp-c)/c, 4)

def aCir(d): return round(0.007854*d**2, 3)

def phi(eu,et,ey):
    if ey <= et <= (eu+ey):
        return round(0.65+0.25/eu*(et-ey), 2)
    else:
        return 0.65 if et < ey else 0.9

def aLstC(dEsq,dLat,nHor,nVer):
    a = round(aCir(dEsq)*2+nHor*aCir(dLat), 3)
    return [a]+[round(aCir(dLat)*2,3) for i in range(nVer)]+[a]

def yLstC(dp,h,nVer):
    yLst = [dp]
    for i in range(1,nVer+1):
        yi = round((h-yLst[i-1]-dp)/(nVer+2-i)+yLst[i-1],0)
        yLst.append(int(yi))
    yLst.append(h-dp)
    return yLst

def pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst):
    eiLst = [round(eu*(c-i)/c, 5) for i in yLst]
    fsLst = [fy*abs(i)/i if abs(i)>ey else es*i for i in eiLst]
    psLst = [fsLst[i] * aLst[i] for i in range(len(aLst))]
    Pc = 0.85*b1*fc*b*c
    Ps = sum(psLst)
    Mc = Pc/2*(h-0.85*c)
    Ms = sum((psLst[i]*(h/2-yLst[i]) for i in range(len(aLst))))
    return [round((Pc+Ps)/1000, 2), round((Mc+Ms)/100000, 2)]

def cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,pnB,yLst):
    c1 = 0
    c2 = max(h/b1, 3*(h-dp))
    PnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)/1000, 2)
    PhiPnMax = PnMax*0.8*0.65
    PnMin = round((-sum(aLst)*fy)/1000, 2)
    PhiPn = pnB+10
    i = 0
    if pnB > PnMin * 0.9:
        pnB = PhiPnMax if pnB >= PhiPnMax else pnB
        while abs(pnB-PhiPn) > 0.1 and i<15:
            c = round((c1+c2)/2,3)
            i += 1
            PMC = pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
            eT = et(h,eu,dp,c)
            Phi = phi(eu,eT,ey)
            PhiPn = (PMC[0])*Phi
            PhiMn = (PMC[1])*Phi
            c2 = c if PhiPn > pnB else c2
            c1 = c if PhiPn < pnB else c1
    else:
        c = 0
        PhiPn = PnMin*0.9
        PhiMn = 0
        Phi = 0.9
    return [round(c, 2), abs(round(PhiMn, 1)), round(PhiPn, 1), Phi]

def cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst):
    mu = round(abs(mu),3)
    pu = round(pu,3)
    PhiPnMin = round((-sum(aLst)*fy)/1000*0.9,1)
    PhiPnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)*0.8*0.65/1000,1)
    if pu<PhiPnMin:
        pu = PhiPnMin
    if pu>PhiPnMax:
        pu = PhiPnMax
    elif abs(pu) <= 0.1:
        return cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,0,yLst)
    e = min(mu/pu,999)
    i = 0
    c2 = 0
    ex = e+1
    c1 = h/b1 if e > 0 else cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,0,yLst)[0]
    while abs(round(e,3)-ex) > 0.001 and i < 15:
        c = round((c1+c2)/2,2)
        i += 1
        PMC = pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
        ex = round((abs(PMC[1]))/(PMC[0]),3)
        c1 = c if ex < e else c1
        c2 = c if ex > e else c2
    e = ex
    eT = round(eu*abs(h-dp-c)/c,4)
    Phi = phi(eu,eT,ey)
    asdf=pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
    phipn = PMC[0]*Phi
    phimn = PMC[1]*Phi
    return [c,abs(round(phimn,1)),round(phipn,1), Phi, e, PhiPnMin, PhiPnMax]

def resumen(aLst, c, b, dp, h, eu, fy, fc, b1, es, ey, yLst):
    PMC = pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst)
    eT = round(eu*abs(h-dp-c)/c, 4)
    Phi = phi(eu, eT, ey)
    PMCpr = pmC(aLst, b, b1, c, es, eu, ey, fc, fy*1.25, h, yLst)
    return [PMC[0]*Phi,PMC[0],PMCpr[0],PMC[1]*Phi,PMC[1],PMCpr[1]]

def FU(pu, mu, pn, mn):
    if abs(mu) < 0.1:
        return abs(pu/(pn+0.01))
    else:
        return max(abs(pu/(pn+0.01)), abs(mu/(mn+0.01)))

def yLstV(h, dp, db):
    # se busca el minimo de niveles barras laterales complementarias
    blat = min(int((h-2*dp-db/4)/25), int((h-2*dp-db/4)/20)+1)
    # se crea lista con dos primeros niveles (1/4*10=2.5 veces el diámetro mayor)
    Y = [dp, max(dp+db/4, 2*dp)]
    #se agrega cada nivel de barras complementarias
    for i in range(blat):
        Y.append(round(Y[-1]+(h-2*dp-db/4)/(blat+1), 0))
    # la función retorna la lista de posiciones de barras completa
    return Y + [h - dp] if Y[-1] < (h-dp) else Y

# función para el cálculo de área requerida asegurando et>=0.005
def areaV(mu, b, b1, h, fc, fy, dp):
    muu = round(mu/(0.9*0.85/100000*fc*b*(h-dp)**2), 3)
    muu = 0.5 if muu > 0.5 else muu
    ulim = round(0.375*b1*(1-0.1875*b1), 3)
    wp = 0 if muu < ulim else round((muu-ulim)/(1-dp/(h-dp)), 3)
    w = 0.375+wp if wp > 0 else round(1-(1-2*muu)**0.5, 3)
    return round(w*0.85*fc*b*(h-dp)/fy, 2)

def listadiam1(A, b, dp, h, dList, v):
    sup = [i for i in range(int(1+(b-2*dp)/15), 2+int((b-2*dp)/10))]
    listadiam = []
    for i in sup:
        n2 = int(i/2) if i>2 else 0
        n1 = i-n2
        for j in range(len(dList)):
            j = dList[j]
            if n2>0:
                for k in range(len(dList)):
                    k = dList[k]
                    if A<=n1*aCir(j)+n2*aCir(k) and j+v>=k>=j-v:
                        listadiam+=[[n1, j, n2, k, round(aCir(j)*n1+aCir(k)*n2, 2)]]
                    else:
                        continue
            else:
                if 1.2*A>=n1*aCir(j)>=A:
                    listadiam+=[[n1, j, n2, 0, round(n1*aCir(j), 2)]]
                else:
                    continue
    return listadiam

def listadiam(A, b, dp, h, dList, v):
    amin = 10*A
    A /= 2
    lista1 = listadiam1(A, b, dp, h, dList, v)
    lista2 = []
    minimos = []
    for i in range(len(lista1)):
        if lista1[i][4]<=1.2*A:
            lista2+=[lista1[i]]
        else:
            continue
    for i in range(len(lista2)):
        L1 = lista2[i]
        ar1= L1[4]
        ar2=round(2*A-ar1, 2)
        ar2 = ar2 if ar2>0 else 0
        lista3 = listadiam1(ar2, b, dp, h, dList, v)
        if lista3 == []:
            continue
        for j in range(len(lista2)):
            L2 = lista3[i]
            if 2*A>L1[4]+L2[4]:
                continue
            else:
                if L1[4]+L2[4]<amin:
                    amin = L1[4]+L2[4]
                    if L2[4]>L1[4]:
                        minimos = [L2, L1, round(amin, 2)]
                    else:
                        minimos = [L1, L2, round(amin, 2)]
    return minimos

def critVC(vigas, columnas):
    crit = lambda lista: round(1.2*sum(lista[0])/sum(lista[1]), 4)
    temp1 = []
    for i in reversed(range(len(columnas))):
        temp2 =[]
        for j in range(len(vigas[0])+1):
            temp3 = [[],[]]
            if j == len(vigas[0]):
                temp3[0].append(vigas[i][len(vigas[0])-1])
            else:
                if j != 0:
                    temp3[0].append(vigas[i][j-1])
                temp3[0].append(vigas[i][j])
            temp3[1].append(columnas[i][j])
            if i != len(columnas)-1:
                temp3[1].append(columnas[i+1][j])
            temp2.append(temp3)
        temp1.append(temp2)
    newlist=temp1[1:]
    for j in newlist:
        for i in j:
            vig=i[0]
            col=i[1]
            z = crit(i)
            for j in range(len(col)):
                col[j]=round(col[j] if z*col[j]<=col[j] else z*col[j], 1)
    critmat=[]
    for i in range(len(temp1)):
        critpis=[]
        for j in range(len(temp1[i])):
            if len(temp1[i][j][0])==1:
                critpis.append(temp1[i][j][0][0])
            else:
                critpis.append(temp1[i][j][0][1])
        critmat.append(critpis)
    return list(reversed(critmat))

def extMat(lista, indice):
    mat1=[]
    for i in lista:
        mat2=[]
        for j in i:
            mat2.append(j[indice])
        mat1.append(mat2)
    return mat1

def replMat(lista1, lista2, indice):
    for i in range(len(lista2)):
        for j in range(len(lista2[i])):
            lista1[i][j][indice]=lista2[i][j]
    return lista1

def matElemV(lista, bmaxV, hmaxV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, ai, deList, v):
    #se itera en la lista
    listaV = []
    for i in lista:
        # se filtra la lista por piso
        tempV=[]
        for j in i:
            elem = optimusVig(j[2],j[3],es,eu,ey,b1,fc,fy,dp,dList,hmaxV,bmaxV,ai,j[5],cH,cS,v)
            #optimusVig(mpp,mnn,es,eu,ey,b1,fc,fy,dp,dList,hmax,bmax,hmin,bmin,ai,lo,cH,cS,v,allVu,deList,wo)
            tempV.append(elem)
        listaV.append(tempV)
    return listaV

def matElemC(listaC, listaV, fc, fy, hmaxC, b1, dp, es, eu, ey, dList, cH, cS):
    matvig=extMat(listaV, 16)
    matcol=extMat(listaC, 3)
    newMatC=critVC(matvig, matcol)
    lista=replMat(listaC, newMatC, 3)
    listaCol=[]
    for i in lista:
        tempC=[]
        for j in i:
            elem=optimusCol(b1, dp, es, eu, ey, fc, fy, j[3], j[0], dList, hmaxC, cH, cS, 1)
            # optimusCol(b1,dp,es,eu, ey, fc, fy, muC, puCmin, puCmax, dList, hmax, cH, cS, H, vu, vue, deList, iguales)
            tempC.append(elem)
        listaCol.append(tempC)
    return listaCol

def Lramas(xList):
    lar=len(xList)
    lista = [xList[0]]
    if lar%2 == 0:
        rango = xList[-1]-xList[0]
        for i in range(1, lar-1):
            if xList[i]-lista[-1]==30:
                lista.append(xList[i])
            elif xList[i]-lista[-1]>30:
                lista.append(xList[i-1])
        lista.append(xList[-1])
        minram = int((len(lista)+1)/2)*2
        maxram = len(xList)
        rlist = [i for i in range(minram, maxram+1, 2)]
        listas = []
        for i in rlist:
            sep = round(rango/(i-1), 1)
            complist = [xList[0]]
            for _ in range(i-1):
                complist.append(sep+complist[-1])
            lista2 = [xList[0]]
            for j in range(1, len(complist)-1):
                dif=999
                for k in xList:
                    if abs(k-complist[j])<dif:
                        dif = abs(k-complist[j])
                        bar = k
                lista2.append(bar)
            lista2.append(xList[-1])
            listas.append(lista2)
    else:
        mid = int(lar/2)
        midL = xList[0:mid+1]
        rango=midL[-1]-midL[0]
        for i in range(1, len(midL)-1):
            if midL[i]-lista[-1]==30:
                lista.append(midL[i])
            elif midL[i]-lista[-1]>30:
                lista.append(midL[i-1])
        lista.append(midL[-1])
        if lista[-2]-(xList[0]+xList[-1])/2<=15:
            lista.remove(lista[-1])
        lista2 = []
        for j in reversed(lista):
            lista2.append(xList[-1]+xList[0]-j)
        lista+=lista2
        listas=[lista]
        minram=len(lista)
        maxram=len(xList)
        rlist=[i for i in range(minram, maxram+1)]
        for i in rlist:
            sep = round(rango/(i-1), 1)
            complist = [xList[0]]
            rango=xList[-1]-xList[0]
            for _ in range(i-1):
                complist.append(sep+complist[-1])
            lista2 = [xList[0]]
            for j in range(1, len(complist)-1):
                dif=999
                for k in xList:
                    if abs(k-complist[j])<dif:
                        dif = abs(k-complist[j])
                        bar = k
                lista2.append(bar)
            lista2.append(xList[-1])
            if rlist[0]==i:
                continue
            else:
                listas.append(lista2)
    for i in listas:
        for j in range(1, len(i)):
            if i[j]-i[j-1]>30:
                listas.remove(i)
    return listas

def estribosV(xList, ramas):
    Lestrib = []
    medio = xList[int(len(xList)/2)]
    for j in ramas:
        mid=int(len(j)/2)
        L1 = j[0:mid]
        if len(j)%2!=0:
            L2 = j[mid+1:]
            cond=1
        else:
            L2 = j[mid:]
            cond=0
        estribos=[[L1[i],L2[i]] for i in range(len(L1))]
        if cond==1:
            estribos+=[[medio]]
        Lestrib.append(estribos)
    return Lestrib

def countram(ramas):
    nramas=[]
    for i in ramas:
        nramas+=[len(i)]
    return nramas

def Lest(h, b, dp, de):
    return round((2*(h+b-4*dp+0.2*de)*10+6.75*de*3.1416+2*max(75, 6*de))/10, 2)

def Ltrab(h, dp, de):
    return round((3.75*de*3.1416+2*max(75, 6*de)+(h+0.2*de-dp)*10)/10, 2)

def vc(fc, b, h, dp):
    return round(0.53*(fc)**0.5*b*(h-dp)/1000, 2)

def ashS(h, b, dp, fc, fy):
    return round(max(0.3*((b*h)/((h-dp)*(b-dp)))*(fc/fy), 0.09*(h-dp)*fc/fy), 3)

def loCol(h, b, H):
    return round(max(h, b, H/6, 45), 1)

def lEmp(fy, db):
    return round(max(0.00073*fy*db if fy<= 4200 else (0.0013*fy-2.4)*db, 30),0)

#revisar, entrada ya es corte
def vprV(h, b, l, mpr1, mpr2, wo):
    return (mpr1+mpr2)/(l/100) + wo*(l/100)/2

def VcAx(Nu, fc, b, h, dp):
    return round(0.53*(1+Nu*1000/(140*h*b))*(fc)**0.5*b*(h-dp)/1000, 1)

def vsLim(fc, b, h, dp):
    return round(2.2*(fc)**0.5*b*(h-dp)/1000,2)

def sRotV(h, dp, db):
    return round(max(min(15, 0.6*db, (h-dp)/4),8), 1)

def sRotC(h, b, db, hx):
    return round(min(max(min(15,0.6*db,(10+(35-hx)/3)),8),10),1)

def sMax(fc, b, h, dp, sm):
    return min(round((h-dp)/4 if vc(fc, b, h, dp)>0.33*(h-dp)*b*(fc/10)**0.5 else (h-dp)/2, 2), sm)

def sEmp(h, dp):
    return round(min(10, (h-dp)/4), 1)

def sCol(db):
    return min(0.6*db, 15)

def cubEstV(h, dp, de, Le):
    lista = []
    for i in Le:
        if len(i)%2 == 0:
            b = i[1]-i[0]
            lista += [Lest(h, b, dp, de)]
        else:
            lista += [Ltrab(h, dp, de)]
    return round(sum(lista)*aCir(de) ,1)

def estribosC(xList):
    lista = []
    ramas = Lramas(xList)
    count = []
    for i in ramas:
        count.append(len(i))
        Lestrib = []
        temp = i
        while len(temp) > 0:
            if len(temp) >= 2:
                Lestrib.append([temp[0],temp[-1]])
                temp.remove(temp[0])
                temp.remove(temp[-1])
            elif len(temp) == 1:
                Lestrib.append([temp[0]])
                temp.remove(temp[0])
            else:
                break
        lista.append(Lestrib)
        Lestrib = []
    return lista, count

def xLst(sup, b, dp):
    mid = int(sup[0] / 2)
    if sup[2]%2==0:
        l1=[sup[1] for i in range(mid)]
        l2=[sup[3] for i in range(sup[2])]
    else:
        l1=[sup[1] for i in range(mid)]
        l2=[sup[3] for i in range(sup[2])]
    lista=l1+l2+l1
    xList=yLstC(dp, b, len(lista)-2)
    return lista, xList

def minEstC(mpr1, mpr2, Nu, H, vu, vue, yList, deList, db, h, b, dp, fy, fc, cS):
    salida1, salida2, salida3 = 0, 0, 0
    H*=100
    vu = vu*1000
    vue = vue*1000
    mpr1*=100000
    mpr2*=100000
    Vc = VcAx(Nu, fc, b, h, dp)*1000
    vupr = round((mpr1+mpr2)/H,1)
    vupr1 = vupr if Nu*1000 < 0.05 * fc * (h * b) else vupr-Vc
    vupr2 = vupr-Vc
    vu1 = round(max((vu-Vc)/0.75, vue/0.6, vupr1/0.75),1)
    vslim = vsLim(fc, b, h, dp)*1000
    lo = loCol(h, b, H)
    # k1 = (H-2*lo)/H --> X incorrecto, para hacer esto se evalúan
    # los cortes de ambosa extremos y se interpola linealmente
    k1=1
    vu2 = round(k1*max((vu-Vc)/0.75, vue/0.6, (vupr1-Vc)/0.75), 1)
    s = round(sCol(db))
    estr = estribosC(yList)
    est = estr[0]
    nRam = estr[1]
    ramas = Lramas(yList)
    if len(ramas)>1:
        srotL = [int(sRotC(h, b, db, l)) for l in [min(k) for k in [[i[j]-i[j-1] for j in range(1,len(i))] for i in ramas]]]
    else:
        ramitas = ramas[0]
        aux1=[ramitas[i]-ramitas[i-1] for i in range(1,len(ramitas))]
        srotL =  [int(sRotC(h, b, db, max(aux1)))]
    sash = round(ashS(h, b, dp, fc, fy), 3)
    sreq = lambda nRam, de: int((nRam*aCir(de))/sash)
    s1L = [[i, j, k, l] for i in range(len(nRam)) for j in deList
           for k in range(8, int(sRotC(h, b, db, srotL[i])+1)) for l in deList
           if vu1 <= round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim and l <= j]
    if s1L==[]:
        return 0
    minimo = 99999999
    for i, j, k, l in s1L:
        ramas1 = est[i]
        l1 = Lest(h, ramas1[0][1]-ramas1[0][0], dp, j)
        l2 = sum([Lest(h, ramas1[m][1]-ramas1[m][0], dp, l) if len(ramas1[m])==2 else Ltrab(h, dp, l)
              for m in range(1,len(ramas1))])
        s1 = int((lo-0.01)/k)+1
        costo = round(2*s1*(l1*aCir(j)+l2*aCir(l))*cS/1000000, 0)
        if costo<minimo:
            minimo=costo
            lista1=[costo, nRam[i], j, k, l, s1, lo]
            salida1=1
    l_rot = lista1[3]
    l_emp = lEmp(fy, db)
    s2L = [[i, j, k] for i in range(len(nRam)) for j in deList for k in range(10, s+1)
           if vu2<=round(nRam[i]*aCir(j)*fy*(h-dp)/k, 1)<=vslim]
    if s2L==[]:
        return 0
    minimo = 99999999
    for i, j, l in s2L:
        ramas1 = est[i]
        s2 = int((H-2*lo-l_emp-0.01)/k)
        dist2 = H-2*lo-l_emp
        l2 = sum([Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                  for m in range(0, len(ramas1))])
        costo = round(s2*l2*aCir(j)*cS/1000000, 0)
        if costo<minimo:
            minimo=costo
            lista2=[costo, nRam[i], j, k, s2, dist2]
            salida2=1
    semp = int(sEmp(h, dp))
    # k2 = l_emp/(2*H)
    k2 = 1
    vu3 = round(k2*max((vu-Vc)/0.75, vue/0.6, (vupr1-Vc)/0.75), 1)
    s3L = [[i, j, k] for i in range(len(nRam)) for j in deList for k in range(5, semp+1)
           if vu3<=round(nRam[i]*aCir(j)*fy*(h-dp)/k, 1)<=vslim]
    if s3L==[]:
        return 0
    minimo = 99999999
    for i, j, k in s3L:
        ramas1 = est[i]
        s3 = int((l_emp-0.01)/k)+1
        l2 = sum([Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                  for m in range(0, len(ramas1))])
        costo = round(s3 * l2 * aCir(j) * cS / 1000000, 0)
        if costo < minimo:
            minimo = costo
            lista3 = [costo, nRam[i], j, k, s3, l_emp]
            salida3=1
    costo_total = lista1[0]+lista2[0]+lista3[0]
    # lista1 --> [n° ramas, de_externo, espaciamiento, de_interno, n° estribos, dist]
    # lista2 --> [n° ramas, de, espaciamiento, n° estribos, dist]
    # lista3 --> [n° ramas, de, espaciamiento, n° estribos, dist]
    # los estribos del empalme corresponden a los mismos de la zona ubicada fuera de la rótula plástica,
    # solo varía su separación.
    salida=salida1+salida2+salida3
    if salida == 3:
        return [costo_total]+lista1[1:]+lista2[1:]+lista3[1:]
    else:
        return 0

def optimusCol(b1, dp, es, eu, ey, fc, fy, muC, puCmin, puCmax, dList, hmax, cH, cS, H, vu, vue, deList, iguales):
    salida=0
    minor = 9999999
    hmax = hmax if hmax>=30 else 30
    hList = [i for i in range(30, hmax+5,5)]
    lista = ([b, h] for b in hList for h in hList if b == h)
    for b, h in lista:
        nH = [i for i in range(int((b-2*dp)/15)-1, int(round((b-2*dp)/10, 0)), 1)]
        nV = nH
        listaND = ([j, k] for j in nH for k in nV if 10 <= (b-2*dp)/(j+1) <= 15 and
                   10 <= (h-2*dp)/(k+1) <= 15 and j == k)
        for j, k in listaND:
            if iguales == 0:
                listaDm = ([l, m] for l in dList for m in dList if m <= l >=16)
            else:
                listaDm = ([l, m] for l in dList for m in dList if m == l >= 16)
            for l, m in listaDm:
                ylist = yLstC(dp, h, k)
                alist = aLstC(l, m, j, k)
                cF = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muC, puCmax, ylist)
                cF2 = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muC, puCmin, ylist)
                fu = round(FU(puCmax, muC, cF[2], cF[1])*100,1)
                fu2 = round(FU(puCmin, muC, cF2[2], cF2[1])*100,1)
                aS = aCir(l)*4+aCir(m)*(2*j+2*k)
                cuan = round(aS/(b*h), 5)
                mpr1 = max(pmC(alist, b, b1, cF[0], es, eu, ey, fc, fy*1.25, h, ylist)[1],
                           pmC(alist, b, b1, cF2[0], es, eu, ey, fc, fy*1.25, h, ylist)[1])
                # print(pmC(alist, b, b1, cF[0], es, eu, ey, fc, fy*1.25, h, ylist)[1],
                #            pmC(alist, b, b1, cF2[0], es, eu, ey, fc, fy*1.25, h, ylist)[1])
                mpr2 = mpr1
                #agregar a entrada H, vu, vue, deList
                if fu < 95 and fu2 < 95 and 0.01 <= cuan <= 0.06:
                    costo = round((aS*cS+(b*h-aS)*cH)/10000, 0)
                    if costo < minor:
                        minor, e = costo, round(cF[1]/(cF[2]+0.001), 3)
                        optimo = [minor, h, b, j, k, l, m, fu, fu2, cuan, cF[0], cF2[0], e, alist, ylist, cF[1], cF[2], muC, puCmax, puCmin]
                        salida=1
                        corte = minEstC(mpr1, mpr2, muC, H, vu, vue, ylist, deList, min(l, m), h, b, dp, fy, fc, cS)
    if salida==1:
        return [optimo, corte]
    else:
        return 0

def minEstV(mpr1, mpr2, vuLsti,vueLsti,vuLstj,vueLstj, xList, deList, db, h, b, lo, dp, fy, fc, cS, wo):
    lo*=100
    Vc = vc(fc, b, h, dp)*1000
    vupr = round(vprV(h, b, lo, mpr1, mpr2,wo),3)*1000
    smax = sMax(fc, b, h, dp, 20)
    srot = int(sRotV(h, dp, db))
    sL1 = [i for i in range(8, int(srot)+1)]
    sL2 = [i for i in range(8, int(smax)+1)]
    vsL = vsLim(fc, b, h, dp)*1000
    ramas = Lramas(xList)
    est = estribosV(xList, ramas)
    nRam = countram(ramas)
    x1 = 2*h
    x2 = lo/2-2*h
    Lout=[]
    for n in range(x1, x1 + 25, 5):
        xa1 = n
        xa2 = (x1 + x2) - xa1
        vsB1 = V2vig(xa1,lo,vuLsti,vueLsti,vuLstj,vueLstj,vupr,Vc,0)
        vsB2 = V2vig(xa1,lo,vuLsti,vueLsti,vuLstj,vueLstj,vupr,Vc,1)
        lista=[[i,j,k,l,m] for i in nRam for j in sL1 for k in deList for l in nRam
        for m in sL2 if vsB1/(fy*(h-dp))<=i*aCir(k)/j<=vsL/(fy*(h-dp))
        and vsB2/(fy*(h-dp))<=l*(aCir(k))/m<=vsL/(fy*(h-dp))]
        minim = 999999999
        if lista!=[]:
            for i in lista:
                nr1, s1, de, nr2, s2 = i
                Lest1 = est[nRam.index(nr1)]
                Lest2 = est[nRam.index(nr2)]
                ns1=int((xa1*2)/s1)
                ns2=int((xa2-0.01)*2/s2)+1
                mini = (cubEstV(h, dp, de, Lest1)*ns1+cubEstV(h, dp, de, Lest2)*ns2)*cS/1000000
                X1 = xa1-5 if xa1 > 2*h else 2*h
                X2 = 2*((x1+x2)-X1)
                if mini < minim:
                    minim = round(mini, 2)
                    #[costo, dist rot, n° ramas, espaciamiento, n° estribos, dist de rotula al centro, n° ramas, espaciamiento, n° estribos, de]
                    Lout = [minim, X1, nr1, s1, ns1, X2, nr2, s2, ns2, de]
    return Lout

dimV=[70,40,40,25]

def optimusVig(mpp,mnn,es,eu,ey,b1,fc,fy,dp,dList,dimV,ai,lo,cH,cS,v,allVu,deList,wo):
    mnn=abs(mnn)
    salida=0
    minim = 99999999
    hmax = dimV[0] if dimV[0]>=30 else 30
    bmax = dimV[1] if dimV[1]>=25 else 25
    hmin = dimV[2] if dimV[2]<=30 else 30
    bmin = dimV[3] if dimV[3]<=25 else 25
    hList = [i for i in range(hmin, hmax+5,5)]
    bList = [i for i in range(bmin, bmax+5,5)]
    lista = ([i, j] for i in hList if i >= 100*lo/16 for j in bList if i >= j and j >= 0.4*i)
    for h, b in lista:
        A1 = areaV(mpp, b, b1, h, fc, fy, dp)
        # print(A1)
        A2 = areaV(mnn, b, b1, h, fc, fy, dp)
        # print(A2)
        L1 = listadiam(A1, b, dp, h, dList, v)
        if L1==[]:
            continue
        L2 = listadiam1(A2, b, dp, h, dList, v)
        mi1 = 10*A2
        lis=[]
        for i in range(len(L2)):
            L=L2[i]
            if L[4]<mi1:
                mi1=L[4]
                lis = L
        if lis==[]:
            continue
        db = max(L1[0][1], L1[0][3])
        ylst = list(yLstV(h, dp, db))
        ylstrev = [(h-i) for i in reversed(ylst)]
        aSLst = [L1[0][4], L1[1][4]]+[ai for i in range(len(ylst)-3)]+[lis[4]]
        alstrev = [lis[4]]+[ai for i in range(len(ylst)-3)]+[L1[1][4], L1[0][4]]
        cuanT = round(sum(aSLst)/(h*b-sum(aSLst)), 4)
        cumin = round(max(0.8/fy*(fc**0.5), 14/fy), 4)
        cuan1 = round((aSLst[0]+aSLst[1])/((b*(h-dp))), 4)
        cuan2 = round(aSLst[-1]/((b*(h-dp))), 4)
        cpn = cPn(aSLst, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylst)
        cpnrev = cPn(alstrev, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylstrev)
        c = cpn[0]
        cond = False
        eT = round(eu*abs(h-dp-c)/c, 4)
        mpr1 = pmC(aSLst, b, b1, cpn[0], es, eu, ey, fc, fy * 1.25, h, ylst)[1]
        mpr2 = pmC(alstrev, b, b1, cpnrev[0], es, eu, ey, fc, fy * 1.25, h, ylstrev)[1]
        db = min([L1[0][1] if L1[0][1]>0 else 99
                 ,L1[0][3] if L1[0][3]>0 else 99
                 ,lis[1] if lis[1]>0 else 99
                 ,lis[3] if lis[3]>0 else 99])
        sup=L1[0]
        xlistV = xLst(sup, 30, 5)[1]
        if 0.025 >= cuan1 >= cumin and 0.025 >= cuan2 >= cumin\
                and cpn[1] >= mnn and cpnrev[1] >= mpp:
            cond = True
            costo = round((sum(aSLst)*cS+(h*b-sum(aSLst))*cH)/10000, 0)
            if costo < minim and cond != False:
                minim = costo
                FU = round(max(mnn/cpn[1], mpp/cpnrev[1]) * 100, 1)
                listaT = [minim, h, b, aSLst, ylst, cuan1, cuan2, ylstrev, alstrev,c , round(abs(mnn),2), round(abs(mpp),2), L1, lis,\
                         cpn[1], cpnrev[1], max(cpn[1],cpnrev[1])]
                corte = minEstV(mpr1,mpr2,allVu[0],allVu[1],allVu[2],allVu[3],xlistV,deList, db,h,  b, lo, dp, fy, fc, cS, wo)
                salida = 1
    if salida == 1:
        return listaT, corte
    else:
        return 0



def XYplotCurv(alst, b, h, dp, eu, fy, fc, b1, es, ey, ylst, ce, mu, pu, mn, pn, titulo):
    PnMax = round((0.85*fc*(h*b-sum(alst))+sum(alst)*fy)/1000, 2)
    PnMaxPr = round(PnMax+sum(alst)*fy*0.25/1000, 2)
    PnMin = sum(alst)*-fy/1000
    phiPnMin = 0.9*sum(alst)*-fy/1000
    PnMinPr = 1.25*sum(alst)*-fy/1000
    C = [0]+[i/50*h for i in range(2, 51)]
    X1 = [0]
    X2 = [0]
    X3 = [0]
    Y1 = [phiPnMin]
    Y2 = [PnMin]
    Y3 = [PnMinPr]
    for c in C[1::]:
        res = resumen(alst, c, b, dp, h, eu, fy, fc, b1, es, ey, ylst)
        X1.append(res[3])
        Y1.append(res[0])
        X2.append(res[4])
        Y2.append(res[1])
        X3.append(res[5])
        Y3.append(res[2])
    X1.append(0)
    X2.append(0)
    X3.append(0)
    Y1.append(Y1[-1])
    Y2.append(PnMax)
    Y3.append(PnMaxPr)
    fig = plt.figure(figsize=[4,6], dpi=200)
    plt.plot(X1, Y1, label='ØMn - ØPn', color='steelblue')
    plt.plot(X2, Y2, label='Mn - Pn', color='crimson')
    plt.plot(X3, Y3, label='Mpr - Ppr', color='forestgreen')
    plt.plot([mu], [pu], marker='x', markersize=10, color='red', label='Mu - Pu', lw='1')
    res1 = resumen(alst, ce, b, dp, h, eu, fy, fc, b1, es, ey, ylst)
    plt.plot([0, mu], [0, pu], ls='--', color='black')
    # plt.plot([mu, mn], [pu, pn], ls='--', color='gray')
    plt.xlabel('Mn[tonf-m]')
    plt.xlim([0, max(X3)+0.1])
    plt.ylabel('Pn[tonf]')
    plt.title(titulo)
    plt.legend()
    plt.grid()
    plt.show()
    fig.savefig(titulo)
    return 0

largosC=[[3,3,3,3],
         [3,3,3,3],
         [3,3,3,3]]

largosV=[[7,7,7],
         [7,7,7],
         [7,7,7]]

dimV = [[[70,40,40,25],[70,40,40,25],[70,40,40,25]],
        [[70,40,40,25],[70,40,40,25],[70,40,40,25]],
        [[70,40,40,25],[70,40,40,25],[70,40,40,25]]]

#falta crear lista completa
def matElemV(lista, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, ai, deList, v):
    #se itera en la lista
    listaV = []
    for i in range(len(lista)):
        # se filtra la lista por piso
        tempV=[]
        for j in range(len(lista[0])):
            elem = optimusVig(lista[i][j][0],lista[i][j][1],es,eu,ey,b1,fc,fy,dp,dList,
                              lista[i][j][5],ai,lista[i][j][3],cH,cS,v,lista[i][j][4],deList,lista[i][j][2])
            cont=0
            while elem == 0 and cont<10:
                cont+=1
                lista[i][j][0]=lista[i][j][0]*1.25
                lista[i][j][1]=lista[i][j][1]*1.25
                elem = optimusVig(lista[i][j][0], lista[i][j][1], es, eu, ey, b1, fc, fy, dp, dList,
                                  lista[i][j][5], ai, lista[i][j][3], cH, cS, v, lista[i][j][4], deList, lista[i][j][2])
            tempV.append(elem)
        listaV.append(tempV)
    return listaV

def matElemC(listaC, listaV, fc, fy, hmaxC, b1, dp, es, eu, ey, dList, cH, cS):
    matvig=extMat(listaV, 16)
    matcol=extMat(listaC, 3)
    newMatC=critVC(matvig, matcol)
    lista=replMat(listaC, newMatC, 3)
    listaCol=[]
    for i in lista:
        tempC=[]
        for j in i:
            elem=optimusCol(b1, dp, es, eu, ey, fc, fy, j[3], j[0], dList, hmaxC, cH, cS, 1)
            # optimusCol(b1,dp,es,eu, ey, fc, fy, muC, puCmin, puCmax, dList, hmax, cH, cS, H, vu, vue, deList, iguales)
            tempC.append(elem)
        listaCol.append(tempC)
    return listaCol

cH, cS, b1, dp, es, ey, eu, fc, fy = 75000,7850000,0.85,5,2100000,0.002,0.003,250,4200
dList, deList = [16,18,22,25,28,32,36],[10,12]

def optimusFrame(tabla, largosC, largosV, dimV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, deList):
    dList=[16,18,22,25,28,32,36]
    deList=[10,12]
    combis = 7
    combi_e = 4
    combi_s = 3
    tab = tabla['body']
    filtro=filtroCV(combis, combi_e, combi_s, tab, largosV, largosC)
    listaV=filtro[0]
    listaC=filtro[1]
    #filtro por piso
    mpp1=[max([max([max(listaV[i][j][0][2], listaV[i][j][1][2]) for j in range(len(listaV[0]))])
                 for k in range(len(listaV[0][0]))]) for i in range(len(listaV))]
    mpp2=[mpp1 for i in range(len(listaV))]
    mpp3=[max(listaV[i][0][0][2], listaV[i][-1][1][2]) for i in range(len(listaV))]
    mnn1=[min([min([min(listaV[i][j][0][3], listaV[i][j][1][3]) for j in range(len(listaV[0]))])
                 for k in range(len(listaV[0][0]))]) for i in range(len(listaV))]
    mnn2=[mnn1 for i in range(len(listaV))]
    mnn3 = [max(listaV[i][0][0][3], listaV[i][-1][1][3]) for i in range(len(listaV))]
    allVuL = [[[listaV[i][j][0][6], listaV[i][j][0][7], listaV[i][j][1][6],
                listaV[i][j][1][7]] for j in range(len(listaV[0]))] for i in range(len(listaV))]
    wo1 = [max([max(listaV[i][j][0][4],listaV[i][j][1][4]) for j in range(len(listaV))]) for i in range(len(listaV))]
    wo2 = [wo1 for i in range(len(listaV))]
    minLo = [min(i) for i in largosV]
    maxLo = [max(i) for i in largosV]
    listaVig = [[[mpp2[i][j],mnn2[i][j],wo2[i][j],largosV[i][j],allVuL[i][j], dimV[i][j]]
       for i in range(len(listaV))] for j in range(len(listaV[0]))]
    print(optimusVig(58.7, 30.3, 2100000, 0.003, 0.002, 0.85, 250, 4200, 5, [16, 18, 22, 25, 28, 32, 36],[60,60,30,30], 1, 7, 75000,
          7850000, 5, listaVig[0][0][4], [10,12], 3))
    # mpp, mnn, hmax, hmin, bmax, bmin, lo, wo, allVu
    print(matElemV(listaVig, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, 1, deList, 5))
    # optimusVig(mpp, mnn, es, eu, ey, b1, fc, fy, dp, dList, hmax, bmax, hmin, bmin, ai, lo, cH, cS, v, allVu, deList, wo)
    # critVC(vigas, columnas)
    # optimusCol(b1, dp, es, eu, ey, fc, fy, muC, puCmin, puCmax, dList, hmax, cH, cS, H, vu, vue, deList, iguales)
    # XYplotCurv(alst, b, h, dp, eu, fy, fc, b1, es, ey, ylst, ce, mu, pu, mn, pn, titulo)
    return 0

# extMat(lista, indice)
# replMat(lista1, lista2, indice)

optimusFrame(tabla, largosC, largosV, dimV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, deList)
# print(optimusVig(2.52,abs(-0.93),2100000,0.003,0.002,0.85,250,4200,5,[16,18,22,25,28,32,36],
#                               [70, 40, 40, 25],1,7,75000,7850000,5,
#                  [[2094.3, 4026.5], [2254.4, 4125.0, 411.1, 2281.6], [-2094.3, -4026.5], [-4125.0, -2254.4, -2281.6, -411.1]],
#                  [10,12],3.19))

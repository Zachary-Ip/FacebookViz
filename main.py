from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [9, 5, 7, 2, 8]

output_file("test.html")

p = figure(title="example")

# render glyph
p.line(x, y)

# show results
show(p)

import numpy as np
from bqplot import *
from bqplot.marks import Graph
from ipywidgets import Layout, VBox, HBox
from relmath import * 


def Rel_bq_npartite(rel_exprs):
    """ 
            M1      M2      M3
        a   --  x       p        g
        b   --  y    /  q  ----- b
        c   \   z  /
              \ w
    """    
    if len(rel_exprs) == 0:
        raise ValueError("Expected a non-empty list !")
    i = 0
    for expr in rel_exprs:
        if not isinstance(expr, Expr):
            raise ValueError("Expected an Expr ! Instead Found as value at index %s this  %s " % (i,expr))
        i += 1

    """
        node_data = [
            {'label': 'A', 'shape': 'circle', 'shape_attrs': {'r': 20}, 'foo': 1},
            {'label': 'Node B', 'shape': 'rect', 'shape_attrs': {'rx': 10, 'ry': 10, 'width': 40}, 'foo': 2},
            {'label': 'C', 'shape': 'ellipse', 'foo': 4},
            {'label': 'D', 'shape': 'rect', 'shape_attrs': {'width': 30, 'height': 30}, 'foo': 100},
        ]    
    """

    texts = []
    node_data = []    
    link_data = []
    x = []
    y = []

    base = 0
    x_distance = 100
    # fake rel
    
    for rel in rel_exprs :
        srel = rel.simp()
        n = len(srel.dom)
        m = len(srel.cod)
        for i in range(n):
            for j in range(m):
                link_data.append({'source': base + i, 'target': base + n + j, 'value': srel.g[i][j].val})
        base += n
    
    i = 0
    for rel in rel_exprs + [rel_exprs[-1].simp().T]:
        srel = rel.simp()
        node_data.extend([{'label':dom, 'r':30} for dom in srel.dom])
        n = len(srel.dom)
        
        x.extend(([(i+1)*x_distance] * n))
        y.extend(reversed(range(n)))

        if i < len(rel_exprs):
            with Q(S):
                texts.append(str(rel))

        i += 1


    fig_layout = Layout(width='960px', height='300px')
    
    xs = LinearScale()
    ys = LinearScale()
    lcs = ColorScale(scheme='Reds')
    
    # TODO !!! WORKS FOR BINOPS ONLY IF I PUT MAGIC 3 NUMBER !!!!!!!!!
    labels = Label(x=[(i*x_distance) + (x_distance/2) for i in range(1, len(rel_exprs)+1)],
                   y=[max(y)+1]*2, scales={'x': xs, 'y': ys},
                text=texts, default_size=26, font_weight='bolder',
                colors=['black'], update_on_move=True)
    

    """
            self.graph.hovered_style = {'stroke': '1.5'}
            self.graph.unhovered_style = {'opacity': '0.4'}
            
            self.graph.selected_style = {'opacity': '1',
                                        'stroke': 'red',
                                        'stroke-width': '2.5'}

    """

    graph = Graph(  node_data=node_data, link_data=link_data, link_type='line',
                    colors=['orange'], directed=False, 
                    scales={'x': xs, 'y': ys, 'link_color': lcs}, 
                    x=x, y=y,  color=['black']*len(node_data))

    return Figure(marks=[graph, labels], layout=fig_layout)    




def BinOp_to_bq(self):

        fig1 = Rel.bq_npartite([self.left, self.right])
        fig2 = Rel.bq_npartite([self])    
        
        return VBox([fig1, fig2])
        

# monkey patching
Rel.bq_npartite = Rel_bq_npartite
BinOp.to_bq = BinOp_to_bq

with Q(S):
    
    M = Rel([
                [0.2, 0.7, 0, 0],
                [0.9,0,0.5,0],
                [0.9,0,0,0]
            ], 
            ['a','b','c'], 
            ['x','y','z','w'],
            name='M')

    
    E = M * M.T
    
print(E)
print(E.simp())
E.to_bq()
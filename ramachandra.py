'''
Program to generate ramachandra plot
'''
from RamachanDraw import fetch, phi_psi, plot

def ramachandra_plot(pdb_id):
    plot(pdb_id)
    phi_psi_dict, ignored_res = phi_psi(fetch(PDB_id), return_ignored=True)

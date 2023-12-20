#Requires mdtraj library

import numpy as np
import mdtraj as md


def abs_contact_order(xyz, atoms_residue, cutoff_nm=.6):
    """Return the absolute contact order."""
    contact_count = 0
    seq_distance_sum = 0
    cutoff_2 = cutoff_nm*cutoff_nm
    N = len(atoms_residue)
    for i in range(N):
        for j in range(N):
            seq_dist = atoms_residue[j] - atoms_residue[i]
            if seq_dist > 0:
                d = xyz[j] - xyz[i]
                if np.dot(d, d) < cutoff_2:
                    seq_distance_sum += seq_dist 
                    contact_count += 1


    if contact_count==0.:
        print("Warning, no contacts found!")
        return 0.

    print("contact_count: ", contact_count)
    print("seq_distance_sum: ", seq_distance_sum)
    return seq_distance_sum/float(contact_count)

traj = md.load("2acy_new.pdb")
print("Atoms: ", traj.n_atoms)
seq_atoms = np.array([a.residue.resSeq for a in traj.top.atoms], dtype=int)

abs_co = abs_contact_order(traj.xyz[0], seq_atoms, cutoff_nm=0.60)

print("Absolute Contact Order: ", abs_co)
print("Relative Contact Order: ", abs_co/traj.n_residues)
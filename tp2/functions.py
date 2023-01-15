from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import string


message = 'CRIStAL (Centre de Recherche en Informatique, Signal et Automatique de Lille) est une unité mixte de recherche (UMR 9189) résultant de la fusion du LAGIS (Laboratoire d’Automatique, Génie Informatique et Signal - UMR 8219) et du LIFL (Laboratoire d’Informatique Fondamentale de Lille - UMR 8022) pour fédérer leurs compétences complémentaires en sciences de l’information. CRIStAL est né le 1er janvier 2015 sous la tutelle du CNRS, de l’Université Lille 1 et de l’Ecole Centrale de Lille en partenariat avec l’Université Lille 3, Inria et l’Institut Mines Telecom. CRIStAL est membre de l’institut de recherches interdisciplinaires IRCICA – USR CNRS 3380 (www.ircica.univ-lille1.fr). L’unité est composée de près de 430 membres (222 permanents et plus de 200 non permanents) dont 22 permanents CNRS et 27 permanents Inria. Les activités de recherche de CRIStAL concernent les thématiques liées aux grands enjeux scientifiques et sociétaux du moment tels que : BigData, logiciel, image et ses usages, interactions homme-machine, robotique, commande et supervision de grands systèmes, systèmes embarqués intelligents, bio-informatique… avec des applications notamment dans les secteurs de l’industrie du commerce, des technologies pour la santé, des smart grids.CRIStAL (Centre de Recherche en Informatique, Signal et Automatique de Lille) est une unité mixte de recherche (UMR 9189) résultant de la fusion du LAGIS (Laboratoire d’Automatique, Génie Informatique et Signal - UMR 8219) et du LIFL (Laboratoire d’Informatique Fondamentale de Lille - UMR 8022) pour fédérer leurs compétences complémentaires en sciences de l’information. CRIStAL est né le 1er janvier 2015 sous la tutelle du CNRS, de l’Université Lille 1 et de l’Ecole Centrale de Lille en partenariat avec l’Université Lille 3, Inria et l’Institut Mines Telecom. CRIStAL est membre de l’institut de recherches interdisciplinaires IRCICA – USR CNRS 3380 (www.ircica.univ-lille1.fr). L’unité est composée de près de 430 membres (222 permanents et plus de 200 non permanents) dont 22 permanents CNRS et 27 permanents Inria. Les activités de recherche de CRIStAL concernent les thématiques liées aux grands enjeux scientifiques et sociétaux du moment tels que : BigData, logiciel, image et ses usages, interactions homme-machine, robotique, commande et supervision de grands systèmes, systèmes embarqués intelligents, bio-informatique… avec des applications notamment dans les secteurs de l’industrie du commerce, des technologies pour la santé, des smart grids.CRIStAL (Centre de Recherche en Informatique, Signal et Automatique de Lille) est une unité mixte de recherche (UMR 9189) résultant de la fusion du LAGIS (Laboratoire d’Automatique, Génie Informatique et Signal - UMR 8219) et du LIFL (Laboratoire d’Informatique Fondamentale de Lille - UMR 8022) pour fédérer leurs compétences complémentaires en sciences de l’information. CRIStAL est né le 1er janvier 2015 sous la tutelle du CNRS, de l’Université Lille 1 et de l’Ecole Centrale de Lille en partenariat avec l’Université Lille 3, Inria et l’Institut Mines Telecom. CRIStAL est membre de l’institut de recherches interdisciplinaires IRCICA – USR CNRS 3380 (www.ircica.univ-lille1.fr). L’unité est composée de près de 430 membres (222 permanents et plus de 200 non permanents) dont 22 permanents CNRS et 27 permanents Inria. Les activités de recherche de CRIStAL concernent les thématiques liées aux grands enjeux scientifiques et sociétaux du moment tels que : BigData, logiciel, image et ses usages, interactions homme-machine, robotique, commande et supervision de grands systèmes, systèmes embarqués intelligents, bio-informatique… avec des applications notamment dans les secteurs de l’industrie du commerce, des technologies pour la santé, des smart grids.CRIStAL (Centre de Recherche en Informatique, Signal et Automatique de Lille) est une unité mixte de recherche (UMR 9189) résultant de la fusion du LAGIS (Laboratoire d’Automatique, Génie Informatique et Signal - UMR 8219) et du LIFL (Laboratoire d’Informatique Fondamentale de Lille - UMR 8022) pour fédérer leurs compétences complémentaires en sciences de l’information. CRIStAL est né le 1er janvier 2015 sous la tutelle du CNRS, de l’Université Lille 1 et de l’Ecole Centrale de Lille en partenariat avec l’Université Lille 3, Inria et l’Institut Mines Telecom. CRIStAL est membre de l’institut de recherches interdisciplinaires IRCICA – USR CNRS 3380 (www.ircica.univ-lille1.fr). L’unité est composée de près de 430 membres (222 permanents et plus de 200 non permanents) dont 22 permanents CNRS et 27 permanents Inria. Les activités de recherche de CRIStAL concernent les thématiques liées aux grands enjeux scientifiques et sociétaux du moment tels que : BigData, logiciel, image et ses usages, interactions homme-machine, robotique, commande et supervision de grands systèmes, systèmes embarqués intelligents, bio-informatique… avec des applications notamment dans les secteurs de l’industrie du commerce, des technologies pour la santé, des smart grids.CRIStAL (Centre de Recherche en Informatique, Signal et Automatique de Lille) est une unité mixte de recherche (UMR 9189) résultant de la fusion du LAGIS (Laboratoire d’Automatique, Génie Informatique et Signal - UMR 8219) et du LIFL (Laboratoire d’Informatique Fondamentale de Lille - UMR 8022) pour fédérer leurs compétences complémentaires en sciences de l’information. CRIStAL est né le 1er janvier 2015 sous la tutelle du CNRS, de l’Université Lille 1 et de l’Ecole Centrale de Lille en partenariat avec l’Université Lille 3, Inria et l’Institut Mines Telecom. CRIStAL est membre de l’institut de recherches interdisciplinaires IRCICA – USR CNRS 3380 (www.ircica.univ-lille1.fr). L’unité est composée de près de 430 membres (222 permanents et plus de 200 non permanents) dont 22 permanents CNRS et 27 permanents Inria. Les activités de recherche de CRIStAL concernent les thématiques liées aux grands enjeux scientifiques et sociétaux du moment tels que : BigData, logiciel, image et ses usages, interactions homme-machine, robotique, commande et supervision de grands systèmes, systèmes embarqués intelligents, bio-informatique… avec des applications notamment dans les secteurs de l’industrie du commerce, des technologies pour la santé, des smart grids.CRIStAL (Centre de Recherche en Informatique, Signal et Automatique de Lille) est une unité mixte de recherche (UMR 9189) résultant de la fusion du LAGIS (Laboratoire d’Automatique, Génie Informatique et Signal - UMR 8219) et du LIFL (Laboratoire d’Informatique Fondamentale de Lille - UMR 8022) pour fédérer leurs compétences complémentaires en sciences de l’information. CRIStAL est né le 1er janvier 2015 sous la tutelle du CNRS, de l’Université Lille 1 et de l’Ecole Centrale de Lille en partenariat avec l’Université Lille 3, Inria et l’Institut Mines Telecom. CRIStAL est membre de l’institut de recherches interdisciplinaires IRCICA – USR CNRS 3380 (www.ircica.univ-lille1.fr). L’unité est composée de près de 430 membres (222 permanents et plus de 200 non permanents) dont 22 permanents CNRS et 27 permanents Inria. Les activités de recherche de CRIStAL concernent les thématiques liées aux grands enjeux scientifiques et sociétaux du moment tels que : BigData, logiciel, image et ses usages, interactions homme-machine, robotique, commande et supervision de grands systèmes, systèmes embarqués intelligents, bio-informatique… avec des applications notamment dans les secteurs de l’industrie du commerce, des technologies pour la santé, des smart grids.'
# Cover file
image_path = './red_fish.png'
# Stego file
stego_path = './stego.png'


def build_Z(R,S):
    im_Diff = S.astype(float) - R.astype(float)
    return np.sum(im_Diff==0)

def build_W(R,S):
    cpt=0
    S_c = S%2==0  # matrice de True si par et False si impair
    R_c = R%2==0  # same
    t_pair =((S_c.astype(int) - R_c.astype(int)) == -1)    # False -  True
    t_impair = ((S_c.astype(int) - R_c.astype(int)) == 1)  # True - False
    for elem in t_pair:
        for value in elem:
            if value:
                cpt+=1

    for elem_i in t_impair:
        for value_i in elem_i:
            if value_i:
                cpt+=1
    return cpt

def condition_X(r,s):
    if s%2==0 and r<s:
        return True
    if s%2!=0 and r>s:
        return True
    else:
        return False


def build_X(R,S):
    cpt=0
    nb_cols = len(S[0])
    nb_rows = len(S)

    for row in range(nb_rows):
        for col in range(nb_cols):
            if condition_X(r=R[row][col],s=S[row][col]):
                cpt+=1
    return cpt

def condition_V(r,s):
    if s%2==0 and r > s+1:
        return True
    if s%2!=0 and r<s:
        return True
    else:
        return False

def build_V(R,S):
    cpt=0
    nb_cols = len(S[0])
    nb_rows = len(S)
    for row in range(nb_rows):
        for col in range(nb_cols):
            if condition_V(r=R[row][col],s=S[row][col]):
                cpt+=1
    return cpt



def resolve_2nd_deg(a,b,c):
    delta = (b**2) - (4*a*c)
    if delta==0:
        return (-b/(2*a),-b/(2*a))
    if delta>0:
        return ( (-b+np.sqrt(delta))/(2*a),  (-b-np.sqrt(delta))/(2*a)  )
    if delta < 0:
        return (0,0)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    #print("Random string of length", length, "is:", result_str)
    return result_str


#****************************************************************************************************************************
#****************************************************************************************************************************


def décoder_taux_insertion(im_stego):
    # Get the image
    pil_image = Image.open(stego_path)
    im_array = np.asarray(pil_image)

    Im = im_array[:,:,2]

    # Get pairs of neighboring pixels
    R = Im[:,:-1]
    S = Im[:,1:]
    #Construction des quatres ensembles dont on va regarder les cardinaux :
    Zp = build_Z(R,S)
    Wp = build_W(R,S)
    Xp = build_X(R,S)
    Vp = build_V(R,S)

    Pp = Xp+Vp+Zp+Wp

    a = float(2*(Wp+Zp))  # beta^2
    b = float(2*(2*Xp-Pp))# beta
    c = float(Vp+Wp-Xp)  # constant
    
    beta = min(resolve_2nd_deg(a=a,b=b,c=c))
    if beta == 0:
        return 0
    # calcul de l'estimation de p
    pEst = beta
    #print('estimated message size (bits):' , pEst*2*512**2)  
    return pEst*2*512**2






def encoder_selon_clé(key,image_path = './red_fish.png'):
    #******************************************
    #            Partie IMAGE
    #******************************************
    # Open the image
    pil_image = Image.open(image_path)
    im_array = np.asarray(pil_image)
    im_stego = np.copy(im_array)

    # Get the blue channel
    blue_channel = im_array[:,:,2]
    w,h = blue_channel.shape
    blue_channel_vec = np.reshape(blue_channel,(w*h))

    #******************************************
    #            Partie MESSAGE
    #******************************************

    message_unicode = str(message)
    bits  = bin(int.from_bytes(message.encode(), 'big'))
    bits = bits[2:]  # ne prend pas les deux premiers
    bit_string  = bin(int.from_bytes(message.encode(), 'big'))
    n = int('0b'+bit_string[2:], 2)
    n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

    #******************************************
    #            Partie Clé
    #******************************************

    key_unicode = str(key)
    key_int = hash(key) 
    nb_bits = len(bits)  # Taille du message

    #******************************************
    #            Partie INSERTION
    #******************************************
    np.random.seed(np.mod(key_int,4294967295))
    index_perm = np.random.permutation(w*h)
    blue_perm = blue_channel_vec[index_perm]
    # Get the LSBs
    lsb = blue_perm&1
    # Write the size on the first 32 bits
    lsb[:32]= list(np.binary_repr(nb_bits, width=32))
    # Write the message after
    lsb[32:32+nb_bits] = list(bits)

    # LSB substitution
    blue_perm_stego = (blue_perm & ~1) | lsb

    blue_stego = np.zeros((w*h))
    # Inverse permutation
    blue_stego[index_perm] = blue_perm_stego
    blue_stego = np.reshape(blue_stego,(w,h))
    blue_stego = blue_stego.astype(dtype=np.uint8)
    im_stego[:,:,2] = blue_stego

    # Save the stego picture
    im_stego_png = Image.fromarray(im_stego)
    im_stego_png.save(stego_path)

    #print('embedding rate:\n',float(nb_bits+32)/(3*h*w), 'bpp\n')
    return im_stego
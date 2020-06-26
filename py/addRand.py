import random

# ===========================================================================
# X, Y, Z座標に乱数を混ぜる
def addRand(rand_xa, rand_xb, rand_ya, rand_yb, rand_za, rand_zb):

    # 頂点の総数
    num = xshade.scene().active_shape().total_number_of_control_points

    for c in range(0, num):

        # 選択頂点か
        flag = xshade.scene().active_shape().vertex(c).active
        if flag == True:

            # 乱数の生成
            rand_x = random.uniform(rand_xa, rand_xb)
            rand_y = random.uniform(rand_ya, rand_yb)
            rand_z = random.uniform(rand_za, rand_zb)

            # 乱数を混ぜる
            pos = xshade.scene().active_shape().vertex(c).position
            xshade.scene().active_shape().vertex(c).position = (pos[0] + rand_x, pos[1] + rand_y, pos[2] + rand_z)

def replaceZero(num):
    try:
        return float(num)
    except:
        return 0

def main():

    rand_xa = TARGET_RAND_XA
    rand_xb = TARGET_RAND_XB
    rand_ya = TARGET_RAND_YA
    rand_yb = TARGET_RAND_YB
    rand_za = TARGET_RAND_ZA
    rand_zb = TARGET_RAND_ZB

    rand_xa = replaceZero(rand_xa)
    rand_xb = replaceZero(rand_xb)
    rand_ya = replaceZero(rand_ya)
    rand_yb = replaceZero(rand_yb)
    rand_za = replaceZero(rand_za)
    rand_zb = replaceZero(rand_zb)

    addRand(rand_xa, rand_xb, rand_ya, rand_yb, rand_za, rand_zb)

main()

import tv_remote

def test_tv_remote_zoo():
	assert(tv_remote.tv_remote(5, 'zoo') == 'DDDDD*UUURRRR**')

def test_tv_remote_oz():
	assert(tv_remote.tv_remote(5, 'oz') == 'DDRRRR*LLLLDDD*')

def test_tv_remote_bozo():
	assert(tv_remote.tv_remote(5, 'bozo') == 'R*DDRRR*LLLLDDD*UUURRRR*')

def test_tv_remote_craycray():
	assert(
		tv_remote.tv_remote(
			5, 
			'supercalifragilisticexpialidocious'
		) == 'DDDRRR*LLLD*U*UUURRRR*LLDDD*UUU*LL*DDR*URR*LLL*DDRR*UUULL*DR*RR*LLD*URR*DD*R*UUL*UL*RR*LDDDD*ULLL*UURRR*ULLL*DDR*URR*U*DDR*UULL*DR*DR*LLLLDD*URRR*'
	)


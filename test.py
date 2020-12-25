print(__import__('base64').b64encode(int(
    (lambda l: l(0xc731656a4659ede265561b53b, '1' * 54, l)) (
        lambda b, e, t, a =
            lambda eye: (lambda smile: eye[:smile][::-1] + '01' + eye[smile+2:])(
                eye.find('10') % len(eye)
            ):
            a(t(b - 1, e, t)) if b else e
    )[::-1],
    2
).to_bytes(13, 'big')).decode('ascii')[-3::-1])

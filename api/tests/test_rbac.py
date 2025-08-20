def test_player_forbidden(client, player_token_headers):
    r = client.post("/clubs/", headers=player_token_headers)
    assert r.status_code == 403


def test_admin_ok(client, admin_token_headers):
    r = client.post("/clubs/", headers=admin_token_headers)
    assert r.status_code == 200

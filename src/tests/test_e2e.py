def test_task_with_incorrect_id_format(test_client):
    result = test_client.get('/task/123-iam-not-a-real-uuid')
    assert result.status_code == 422

def test_get_nonexistent_task(test_client):
    result = test_client.get('/task/ad347cf1-74a8-447e-99b5-12dad28baa3d')
    assert result.status_code == 404

def test_create_task(test_client):
    fake_task_body = {
            'title': 'my test task',
            'description': 'make sure this test does not fail'
        }
    result = test_client.post(
        '/task',
        json=fake_task_body
    
    )
    assert result.status_code == 201
    assert result.json().get('title')== fake_task_body.get('title')
    assert result.json().get('description') == fake_task_body.get('description')
  
def test_get_task_by_criteria(test_client):
    result = test_client.get('/tasks?title=my test task')
    assert result.status_code == 200
    assert(len(result.json())) > 0


    
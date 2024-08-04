let scene, camera, renderer, world;
const balls = [];
const MAX_BALLS = 5;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('scene-container').appendChild(renderer.domElement);

    world = new CANNON.World();
    world.gravity.set(0, -0.1, 0);

    camera.position.z = 10;

    const light = new THREE.PointLight(0xffffff, 1, 100);
    light.position.set(0, 0, 10);
    scene.add(light);

    const ambientLight = new THREE.AmbientLight(0x404040);
    scene.add(ambientLight);

    // Add event listener for mouse click
    renderer.domElement.addEventListener('click', onMouseClick, false);

    animate();
}

function onMouseClick(event) {
    // Calculate mouse position in normalized device coordinates
    const mouse = new THREE.Vector2();
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

    // Create a ball at the clicked position
    addBall(mouse);
}

function addBall(mousePosition) {
    if (balls.length >= MAX_BALLS) {
        const oldestBall = balls.shift();
        scene.remove(oldestBall.mesh);
        world.removeBody(oldestBall.body);
    }

    fetch('/cpu_usage')
        .then(response => response.json())
        .then(data => {
            const radius = 0.3 + (data.cpu_usage / 100) * 0.7;
            const ballShape = new CANNON.Sphere(radius);
            const ballBody = new CANNON.Body({
                mass: 1,
                shape: ballShape,
            });

            // Calculate ball position based on mouse click
            const vector = new THREE.Vector3(mousePosition.x, mousePosition.y, 0.5);
            vector.unproject(camera);
            const dir = vector.sub(camera.position).normalize();
            const distance = -camera.position.z / dir.z;
            const pos = camera.position.clone().add(dir.multiplyScalar(distance));

            ballBody.position.copy(pos);
            world.addBody(ballBody);

            const ballGeometry = new THREE.SphereGeometry(radius, 32, 32);
            const ballMaterial = new THREE.MeshPhongMaterial({ 
                color: Math.random() * 0xffffff,
                shininess: 100
            });
            const ballMesh = new THREE.Mesh(ballGeometry, ballMaterial);
            ballMesh.position.copy(pos);
            scene.add(ballMesh);

            balls.push({ body: ballBody, mesh: ballMesh });
        });
}

function animate() {
    requestAnimationFrame(animate);
    world.step(1 / 60);
    balls.forEach(ball => {
        ball.mesh.position.copy(ball.body.position);
        ball.mesh.quaternion.copy(ball.body.quaternion);
    });
    renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

init();

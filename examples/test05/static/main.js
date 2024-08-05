let scene, camera, renderer, world;
const balls = [];
const MAX_BALLS = 5;
let currentGravity = -0.1;
let currentOpacity = 1.0;

function addRandomBackground() {
    console.log("Starting addRandomBackground function");
    const loader = new THREE.TextureLoader();
    const picsumUrl = `https://picsum.photos/${window.innerWidth}/${window.innerHeight}`;
    console.log("Fetching image from URL:", picsumUrl);
    loader.load(
        picsumUrl,
        function(texture) {
            console.log("Texture loaded successfully");
            const aspectRatio = window.innerWidth / window.innerHeight;
            console.log("Aspect ratio:", aspectRatio);
            const planeGeometry = new THREE.PlaneGeometry(20 * aspectRatio, 20);
            const planeMaterial = new THREE.MeshBasicMaterial({ map: texture, side: THREE.DoubleSide });
            const planeMesh = new THREE.Mesh(planeGeometry, planeMaterial);
            planeMesh.position.set(0, 0, -5);
            console.log("Background plane created and positioned");
            scene.add(planeMesh);
            console.log("Background plane added to scene");
        },
        undefined,
        function(error) {
            console.error("Error loading texture:", error);
        }
    );
}
function init() {
    console.log("Initializing scene");
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('scene-container').appendChild(renderer.domElement);

    console.log("Adding random background");
    addRandomBackground();

    world = new CANNON.World();
    world.gravity.set(0, currentGravity, 0);
    console.log("Physics world created with gravity:", currentGravity);

    camera.position.z = 10;
    console.log("Camera positioned at z =", camera.position.z);

    const light = new THREE.PointLight(0xffffff, 1, 100);
    light.position.set(0, 0, 10);
    scene.add(light);
    console.log("Point light added to scene");

    const ambientLight = new THREE.AmbientLight(0x404040);
    scene.add(ambientLight);
    console.log("Ambient light added to scene");

    renderer.domElement.addEventListener('click', onMouseClick, false);
    renderer.domElement.addEventListener('wheel', onMouseWheel, false);
    window.addEventListener('keydown', onKeyDown, false);
    console.log("Event listeners added");

    animate();
}

function onMouseClick(event) {
    console.log("Mouse clicked at:", event.clientX, event.clientY);
    const mouse = new THREE.Vector2();
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    addBall(mouse);
}

function onMouseWheel(event) {
    event.preventDefault();
    if (event.deltaY < 0) {
        currentGravity *= 1.25;
    } else {
        currentGravity *= 0.75;
    }
    console.log("Gravity adjusted to:", currentGravity);
    world.gravity.set(0, currentGravity, 0);
}

function onKeyDown(event) {
    console.log("Key pressed:", event.key);
    if (event.key === 'ArrowUp') {
        currentOpacity = Math.min(currentOpacity + 0.1, 1.0);
        updateBallOpacity();
    } else if (event.key === 'ArrowDown') {
        currentOpacity = Math.max(currentOpacity - 0.1, 0.0);
        updateBallOpacity();
    }
    console.log("Current opacity:", currentOpacity);
}

function updateBallOpacity() {
    balls.forEach(ball => {
        ball.mesh.material.opacity = currentOpacity;
        ball.mesh.material.transparent = currentOpacity < 1.0;
    });
    console.log("Ball opacity updated for", balls.length, "balls");
}

function addBall(mousePosition) {
    console.log("Adding ball at mouse position:", mousePosition);
    if (balls.length >= MAX_BALLS) {
        console.log("Max balls reached, removing oldest ball");
        const oldestBall = balls.shift();
        scene.remove(oldestBall.mesh);
        world.removeBody(oldestBall.body);
    }

    fetch('/cpu_usage')
        .then(response => response.json())
        .then(data => {
            console.log("CPU usage data received:", data);
            const radius = 0.3 + (data.cpu_usage / 100) * 0.7;
            const ballShape = new CANNON.Sphere(radius);
            const ballBody = new CANNON.Body({
                mass: 1,
                shape: ballShape,
            });

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
                shininess: 100,
                opacity: currentOpacity,
                transparent: currentOpacity < 1.0
            });
            const ballMesh = new THREE.Mesh(ballGeometry, ballMaterial);
            ballMesh.position.copy(pos);
            scene.add(ballMesh);

            balls.push({ body: ballBody, mesh: ballMesh });
            console.log("Ball added, total balls:", balls.length);
        })
        .catch(error => console.error("Error fetching CPU usage:", error));
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
    console.log("Window resized");
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

console.log("Starting initialization");
init();
